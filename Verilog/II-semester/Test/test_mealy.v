module seq_detector(input clk, reset, x, output reg y);
    parameter S0 = 2'b00;
    parameter S1 = 2'b01;
    parameter S2 = 2'b10;

    reg [1:0] state, next_state;

    always @(posedge clk or posedge reset) begin
        if(reset) begin
          state <= S0;
        end
        else begin
          state <= next_state;
        end
    end

    always @(*) begin
        y = 0;
        case (state)
           S0 : next_state = (x == 1) ? S1 : S0;
           S1 : next_state = (x == 0) ? S2 : S1;
           S2 : begin
                if(x == 1) begin
                  next_state = S1;
                  y = 1;
                end
                else begin
                  next_state = S0;
                  y = 0;
                end
           end
            default: next_state = S0;
        endcase
    end
endmodule

module seq_detector_tb;
    reg clk, reset, x;
    wire y;

    seq_detector uut(.clk(clk), .x(x), .reset(reset), .y(y));
    always #5 clk = ~clk;

    initial begin
        $monitor("Time=%0t | x=%b | reset=%b | state=%b | y=%b", $time, x, reset, uut.state, y);
        clk = 0; reset = 1; x = 0;
        #12 reset = 0;

        @(negedge clk) x = 1;
        @(negedge clk) x = 0;
        @(negedge clk) x = 1;
        #10; 
        $finish;
    end
    initial begin
        $dumpfile("test_mealy.vcd");
        $dumpvars(0, seq_detector_tb);
    end
endmodule