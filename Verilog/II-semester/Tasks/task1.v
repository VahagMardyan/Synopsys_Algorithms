module task_1(input a, b, output y);
    assign y = (~a & b) | (a & ~b);
endmodule

module task1_tb;
    reg a,b;
    wire y;
    task_1 uut(.a(a), .b(b), .y(y));
    initial begin
        $monitor("Time=%0t | a=%b | b=%b | y=%b", $time, a,b,y);
        a = 0; b = 0; #10;
        a = 0; b = 1; #10;
        a = 1; b = 0; #10;
        a = 1; b = 1; #10;
        $finish;
    end
endmodule