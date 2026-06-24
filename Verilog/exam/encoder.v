module encoder_42 (
    input [3:0] d, output reg [1:0] y
);
    always @(*) begin
        case (d)
           4'b0001 : y = 2'b00;
           4'b0010 : y = 2'b01;
           4'b0100 : y = 2'b10;
           4'b1000 : y = 2'b11;
            default: y = 2'bxx;
        endcase
    end
endmodule

module encoder_42_tb;
    reg [3:0] data;
    wire [1:0] y;
    encoder_42 uut(.d(data), .y(y));
    initial begin
        $monitor("Time=%0t | data=%b | y=%b", $time, data, y);
        data = 4'b0001;
        #10;
        data = 4'b0010;
        #10;
        data = 4'b0100;
        #10;
        data = 4'b1000;
        #20;
        $finish;
    end
endmodule