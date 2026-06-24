// 101 Assume that posedge clock posedge reset
module fsm_moore (
    input x, clk, reset, output reg y
);
    parameter s0 = 2'b00; // start
    parameter s1 = 2'b01; // 1
    parameter s2 = 2'b10; // 10
    parameter s3 = 2'b11; // 101 Found

    reg [1:0] state, next_state;
    always @(posedge clk or posedge reset) begin
        if(reset)
            state <= s0;
        else
            state <= next_state;
    end

    always @(*) begin
        case (state)
           s0 : next_state = (x == 1) ? s1 : s0;
           s1 : next_state = (x == 0) ? s2 : s1;
           s2 : next_state = (x == 1) ? s3 : s0;
           s3 : next_state = (x == 1) ? s1 : s2;
            default: next_state = s0;
        endcase
    end
    always @(*) begin
        y = (state == s3);
    end
endmodule

module fsm_moore_tb;
    reg x, clk, reset;
    wire y;
    fsm_moore uut(.x(x), .clk(clk), .reset(reset), .y(y));
    always #5 clk = ~clk;
    initial begin
        $monitor("Time=%0t | reset=%b | x=%b | state=%b | y=%b", $time, reset, x, uut.state, y);
        clk = 0; x = 0; reset = 1;
        #7 reset = 0;
        @(negedge clk) x = 1;
        @(negedge clk) x = 0;
        @(negedge clk) x = 1;
        #20;
        $finish;
    end
endmodule