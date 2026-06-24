module Moore(input x, clk, reset, output reg y);
  parameter S0 = 3'b000;
  parameter S1 = 3'b001;
  parameter S2 = 3'b010;
  parameter S3 = 3'b011;
  parameter S4 = 3'b100;

  reg [2:0] state, next_state;

  always @(posedge clk or negedge reset) begin
      if(!reset) begin
        state <= S0;
      end
      else  begin
        state <= next_state;
      end
  end

  always @(*) begin
    case (state)
      S0 : next_state = (x == 1) ? S1 : S0;
      S1 : next_state = (x == 1) ? S2 : S0;
      S2 : next_state = (x == 0) ? S3 : S2;
      S3 : next_state = (x == 1) ? S4 : S0;
      S4 : next_state = (x == 1) ? S2 : S0;
      default: next_state = S0;
    endcase
  end

  always @(*) begin
    y = (state == S4);
  end
endmodule

// module Moore_tb;
//   reg x, clk, reset;
//   wire y;
//   Moore uut(.x(x), .clk(clk), .reset(reset), .y(y));
//   always #5 clk = ~clk;
//   initial begin
//     $monitor("Time=%0t | x=%b | reset=%b | state=%b | y=%b", $time, x, reset, uut.state, y);
//     clk = 0; reset = 0; x = 0;
//     #12 reset = 1;
//     @(negedge clk) x = 1;
//     @(negedge clk) x = 1;
//     @(negedge clk) x = 0;
//     @(negedge clk) x = 1;
//     #10;
//     $finish;
//   end
// endmodule