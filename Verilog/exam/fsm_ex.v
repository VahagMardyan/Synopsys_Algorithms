module fsm_moore(input x, clk, reset, output reg y);
    parameter s0 = 3'b000; // start
    parameter s1 = 3'b001; // 1
    parameter s2 = 3'b010; // 10
    parameter s3 = 3'b011; // 100
    parameter s4 = 3'b100; // 1001
    parameter s5 = 3'b101; // 10010
    
    reg [3:0] state, next_state;

    always @(posedge clk or posedge reset) begin
        if(reset) begin
          state <= s0;
        end
        else begin
          state <= next_state;
        end
    end

    always @(*) begin
      case (state)
       s0 : next_state = (x == 1) ? s1 : s0;
       s1 : next_state = (x == 0) ? s2 : s1;
       s2 : next_state = (x == 0) ? s3 : s2;
       s3 : next_state = (x == 1) ? s4 : s0;
       s4 : next_state = (x == 0) ? s5 : s1;
       s5 : next_state = (x == 1) ? s1 : s3;
        default: next_state = s0;
      endcase
    end

    always @(*) begin
      y = (state == s5) ? 1 : 0;
    end
endmodule

module fsm_moore_tb;
    reg x, clk, reset;
    wire y;
    fsm_moore uut(.x(x), .clk(clk), .reset(reset), .y(y));

    always #5 clk = ~clk;

    initial begin
        // $monitor("Time=%0t | x=%b | reset=%b | state=%b | y=%b", $time, x, reset, uut.state, y);
        x = 0; reset = 1; clk = 0;
        #10 reset = 0;
        @(negedge clk) x = 1;
        @(negedge clk) x = 0;
        @(negedge clk) x = 0;
        @(negedge clk) x = 1;
        @(negedge clk) x = 0;
        @(negedge clk) x = 1;
        #10 $finish;
    end
    initial begin
      $dumpfile("fsm.vcd");
      $dumpvars(0, fsm_moore_tb);
    end
endmodule