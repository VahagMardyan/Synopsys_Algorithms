module example(
    input a, b,c ,
    output y
);
assign y = a & b | c;
endmodule

module test_bench ();

reg a, b, c;
wire y;

example dut(a,b,c,y);

initial begin
    for(integer i=0; i<8; i++) begin
        {a,b,c} = i[2:0];
        #5;
        $display("a=%b b=%b c=%b y=%b", a, b, c, y);
    end
end
    
endmodule