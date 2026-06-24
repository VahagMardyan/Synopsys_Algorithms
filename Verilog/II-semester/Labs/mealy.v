// Mealy machine
// 00011 (posedge clk, posedge set)

module mealy (
    input x, clk, set, output reg y
);
    parameter s0 = 3'b000; // start
    parameter s1 = 3'b001; // 0
    parameter s2 = 3'b010; // 00
    parameter s3 = 3'b011; // 000
    parameter s4 = 3'b100; // 0001

    reg [2:0] state, next_state;

    always @(posedge clk or posedge set) begin
        if(set) 
            state <= s0;
        else
            state <= next_state;
    end
    always @(*) begin
        y = 1'b0;
        case (state) 
            s0 : next_state <= (x == 0) ? s1 : s0;
            s1 : next_state <= (x == 0) ? s2 : s0;
            s2 : next_state <= (x == 0) ? s3 : s0;
            s3 : next_state <= (x == 1) ? s4 : s3;
            s4 : begin
                if(x == 1) begin
                    next_state <= s0;
                    y = 1'b1;
                end
                else begin
                    y = 1'b0;
                end
            end
            default : next_state = s0;
        endcase
    end
endmodule

module mealy_tb;
    reg clk, set, x;
    wire y;
    mealy uut(.clk(clk), .x(x), .set(set), .y(y));

    always #5 clk = ~clk;

    initial begin
        $monitor("Time=%0t | x=%b | set=%b | state = %b | y=%b", $time, x, set, uut.state, y);
        clk = 0; set = 1; x = 0;
        #12 set = 0;
        @(negedge clk) x = 0;
        @(negedge clk) x = 0;
        @(negedge clk) x = 0;
        @(negedge clk) x = 1;
        @(negedge clk) x = 1;
        #10;
        $finish;
    end
endmodule

