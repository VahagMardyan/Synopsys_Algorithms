// 101 Assume negedge clock negedge set

module fsm_mealy (
    input x, clk, set, output reg y
);
    parameter s0 = 2'b00; // start
    parameter s1 = 2'b01; // 1
    parameter s2 = 2'b10; // 10;
    
    reg [1:0] state, next_state;
    
    always @(negedge clk or negedge set) begin
        if(!set)
            state <= s0;
        else
            state <= next_state;
    end

    always @(*) begin
        case (state)
            s0 : next_state = (x == 1) ? s1 : s0;
            s1 : next_state = (x == 0) ? s2 : s1;
            s2 : next_state = (x == 1) ? s1 : s0;
            default: next_state = s0;
        endcase
    end
    always @(*) begin
        y = (state == s2 && x == 1);
    end
endmodule

module fsm_mealy_tb;
    reg x, clk, set;
    wire y;
    fsm_mealy uut(.x(x), .clk(clk), .set(set), .y(y));
    
    always #5 clk = ~clk;

    initial begin
        $monitor("Time=%0t | set=%b | x=%b | state=%b | y=%b", $time, set, x, uut.state, y);
        clk = 1; x = 0; set = 0;
        #13 set = 1;
        @(posedge clk) x = 1;
        @(posedge clk) x = 0;
        @(posedge clk) x = 1;
        #27 $finish;
    end
    initial begin
        $dumpfile("mealy.vcd");
        $dumpvars(0, fsm_mealy_tb);
    end
endmodule