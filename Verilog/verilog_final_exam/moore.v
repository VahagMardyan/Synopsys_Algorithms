// 010001 Moore FSM
module moore(
    input clk,
    input rst,
    input in,
    output reg out
);

    // Binary
    
    localparam S0 = 3'b000, // Start / Error
               S1 = 3'b001, // 0
               S2 = 3'b010, // 01
               S3 = 3'b011, // 010
               S4 = 3'b100, // 0100
               S5 = 3'b101, // 01000
               S6 = 3'b110; // 010001

    /* 
    // Gray Code
    localparam S0 = 3'b000,
               S1 = 3'b001,
               S2 = 3'b011,
               S3 = 3'b010,
               S4 = 3'b110,
               S5 = 3'b111,
               S6 = 3'b101;
    */

    /* 
    // One-Hot
    localparam S0 = 7'b0000001,
               S1 = 7'b0000010,
               S2 = 7'b0000100,
               S3 = 7'b0001000,
               S4 = 7'b0010000,
               S5 = 7'b0100000,
               S6 = 7'b1000000;
    reg [6:0] current_state, next_state;
    */
    
    reg [2:0] current_state, next_state;

    always @(posedge clk or posedge rst) begin
        if(rst) begin
          current_state <= S0;
        end
        else begin
          current_state <= next_state;
        end
    end

    always @(*) begin
      case (current_state) 
        S0: next_state = (in == 0) ? S1 : S0;
        S1: next_state = (in == 1) ? S2 : S1;
        S2: next_state = (in == 0) ? S3 : S0;
        S3: next_state = (in == 0) ? S4 : S2;
        S4: next_state = (in == 0) ? S5 : S2;
        S5: next_state = (in == 1) ? S6 : S1;
        S6: next_state = (in == 0) ? S1 : S0; 
        
        default: next_state = S0;
      endcase
    end

    always @(*) begin
        if(current_state == S6) begin
          out = 1'b1;
        end
        else begin
          out = 1'b0;
        end
    end
endmodule

module mealy_tb;
  reg clk, in, rst;
  wire out;
  moore dut(.in(in), .clk(clk), .rst(rst), .out(out));
  
  initial forever #5 clk = ~clk;
  
  initial begin
    $monitor("time=%0t | rst=%b | in=%b | state=%b | out=%b", $time, rst, in, dut.current_state, out);
    clk = 0; rst = 1; in = 0;
    #12 rst = 0;
    // 010001
    @(negedge clk) in = 0;
    @(negedge clk) in = 1;
    @(negedge clk) in = 0;
    @(negedge clk) in = 0;
    @(negedge clk) in = 0;
    @(negedge clk) in = 1;
    #10;
    $finish;
  end
endmodule