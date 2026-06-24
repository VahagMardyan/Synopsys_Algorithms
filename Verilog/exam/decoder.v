module decoder_24 (
    input [1:0] d, output reg [3:0] y
);
    always @(*) begin
        y = 4'b0000;
        case (d)
           2'b00 : y[0] = 1;
           2'b01 : y[1] = 1;
           2'b10 : y[2] = 1;
           2'b11 : y[3] = 1;
            default: y = 4'bx;
        endcase
    end
endmodule

module decoder_24_tb;
    reg [1:0] data;
    wire [3:0] y;
    decoder_24 uut(.d(data), .y(y));
    initial begin
        $monitor("Time=%0t | data=%b | y=%b", $time, data, y);
        for(integer i=0; i<4; i = i+1) begin
            data = i[1:0];
            #10;
        end
        #13 $finish;
    end
endmodule