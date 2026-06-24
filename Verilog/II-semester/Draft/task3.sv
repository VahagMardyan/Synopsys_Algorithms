module logic_cell(input a, b, c, output o);
    // // or(o, a & b | ~c, a & b & c);
    and(x, a, b);
    not(y, c);
    or(z, x, y);
    and(e, c, x);
    or(o, z, e);
endmodule

module logic_cell_tb();
    reg a;
    reg b;
    reg c;
    wire o;
    logic_cell dut(.a(a), .b(b), .c(c), .o(o));
    initial begin
    //    $display("i | a | b | c | out");
        $dumpfile("task3.vcd");
        $dumpvars(0, logic_cell_tb);
        for(integer i = 0; i < 8; i = i + 1) begin
            {a, b, c} = i[2:0]; 
            #5;
            $display("%d | a=%b | b=%b | c=%b | out=%b", i, a, b, c, o);
        end
        $finish;
    end
endmodule
