module sum(input [4:0]a,b,
           output [9:0] y,
           input [1:0] op
    );
assign y = 
    ( op == 2'b00) ? a + b:
    ( op == 2'b01) ? a - b:
    ( op == 2'b10) ? a * b:
    a / b;
endmodule
