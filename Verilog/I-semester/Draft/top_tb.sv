module tb();
    reg [4:0] a,b;
    reg [1:0] op;
    wire [9:0] y;
    sum dut(a,b,y,op);

    task drive (
        input [4:0] a1, b1,
        input [2:0] op1
    );

    a = a1;
    b = b1;
    op = op1;
    #5;
    $display ("a=%d, b=%d, op=%d, y=%d", a, b, op, y);
    endtask

    initial begin
      a = 4;
      b = 5;
      op = 0;
      #5;
      drive(4,5,0);
      drive(1,99,1);
      drive(10,9,2);
    end
endmodule