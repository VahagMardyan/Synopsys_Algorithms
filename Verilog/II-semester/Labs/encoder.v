module encoder_42 (input [3:0] in, output reg [1:0] out);
    always @(*) begin
        case (in)
            4'b0001 : out = 2'b00;
            4'b0010 : out = 2'b01;
            4'b0100 : out = 2'b10;
            4'b1000 : out = 2'b11;
            
            default: out = 2'bxx;
        endcase
    end
endmodule

module encoder_42_tb;
    reg [3:0] in;
    wire [1:0] out;

    encoder_42 uut(.in(in), .out(out));

    initial begin
      in = 4'b0001;

        /*
            in = 4'b0001;
            in = 4'b0010;
            in = 4'b0100;
            in = 4'b1000;
        */

      while(in <= 4'b1000 && in != 0) begin
            #10;
            in = in << 1;
      end
    end

    initial begin
        // $dumpfile("lab6.vcd");
        // $dumpvars(0, encoder_42_tb);
        $monitor("Time=0%t | input=%b | output=%b", $time, in, out);
    end
endmodule