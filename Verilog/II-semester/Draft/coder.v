module coder (
    input wire [3:0] a,
    output reg[1:0] q
);
    always @(*) begin
        case (a)
            4'b0001 : q = 2'b00;
            4'b0010 : q = 2'b01;
            4'b0100 : q = 2'b10;
            4'b1000 : q = 2'b11; 
            default: q = 0;
        endcase
    end
endmodule

module coder_tb;
    reg [3:0] a;
    wire [1:0] q;
    integer i;
    coder uut(.a(a), .q(q));
    initial begin
        a = 4'b0001;
        #10;
        a = 4'b0010;
        #10;
        a = 4'b0100;
        #10;
        a = 4'b1000;
    end
    initial begin
        $monitor("Time=0%t | a=%b | out=%b", $time, a, q);
    end
endmodule
