module sum(
    input [4:0] a,b,
    input [1:0] op,
    output [9:0] y
);
    assign y =
        (op == 2'b00) ? a + b:
        (op == 2'b01) ? a - b:
        (op == 2'b10) ? a * b:
        a / b;
endmodule

module tb();
    reg [4:0] a,b;
    reg [1:0] op;
    wire [9:0] y;
    sum dut (a, b, op, y);

    task drive (
      input [4:0] a1, b1,
      input [1:0] op1 
    );
    begin
        a = a1;
        b = b1;
        op = op1;
        #5;
        $display("a=%d, b=%d, op=%d, y=%d", a, b, op, y);
    end
    endtask //drive
    initial begin
        a = 4;
        b = 5;
        op = 0;
        #5;
        $display("a=%d, b=%d, op=%d, y=%d", a, b, op, y);
        drive(5, 4, 1);
        drive(10, 9, 2);
        drive(90, 9, 3);
    end
endmodule
