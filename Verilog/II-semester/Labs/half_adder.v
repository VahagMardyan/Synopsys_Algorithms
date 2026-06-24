// Half Adder

module halfadder(
    a, b, sum, c_out
);
    input a, b;
    output sum, c_out;
    assign sum = a ^ b;
    assign c_out = a & b;
endmodule

module halfadder_tb;
    reg a, b;
    wire s, cout;
    halfadder uut(
        .a(a), .b(b), .sum(s), .c_out(cout)
    );
    initial begin
        $monitor("Time=%0t | a=%b | b=%b | s=%b | carry=%b", $time, a, b, s, cout);
        for(integer i=0;i<4;i=i+1) begin
            {a,b} = i[1:0];
            #10;
        end
        $finish;
    end
endmodule