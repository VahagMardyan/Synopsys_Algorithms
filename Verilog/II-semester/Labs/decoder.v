// 2:4 decoder (2 inputs and 4 outputs)
module decoder_24 (
    in, out
);
    input wire [1:0] in;
    output reg [3:0] out;
    always @(*) begin
        case (in)
            2'b00 : out = 4'b1000;
            2'b01 : out = 4'b0100;
            2'b10 : out = 4'b0010;
            2'b11 : out = 4'b0001;
            default: out = 4'b0000;
        endcase
    end
endmodule

module decoder_24_tb;
    reg [1:0] in;
    wire [3:0] out;

    decoder_24 uut(.in(in), .out(out));

    initial begin
        /*
            in = 2'b00;
            in = 2'b01;
            in = 2'b10;
            in = 2'b11;
        */
        for(integer i=0; i<4; i = i+1) begin
          in = i[1:0];
          #10;
        end
        $finish;
    end

    initial begin
        // $dumpfile("decoder_24.vcd");
        // $dumpvars(o, decoder_24_tb);
        $monitor("Time=0%t | input=%b | output=%b", $time, in, out);
    end
endmodule