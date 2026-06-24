module logic_cell(input a, b, c, output o);
    // // or(o, a & b | ~c, a & b & c);
    // and(x, a, b);
    // not(y, c);
    // or(z, x, y);
    // and(e, c, x);
    // or(o, z, e);

    // // // After minimization by Karnaugh map, we get
    // // or(o, ~c, a&b);

    and(x, a, b);
    not(y, c);
    or(o, x, y);
endmodule

// module logic_cell_tb();
//     reg a;
//     reg b;
//     reg c;
//     wire o;
//     logic_cell dut(.a(a), .b(b), .c(c), .o(o));
//     initial begin
//         for(integer i = 0; i < 8; i = i + 1) begin
//             {a, b, c} = i[2:0]; 
//             #5;
//         end
//         $finish;
//     end
//     initial begin
//         // $dumpfile("lab3.vcd");
//         // $dumpvars(0, logic_cell_tb);
//         $monitor("Time=0%t | a=%b | b=%b | c=%b | out=%b", $time, a, b, c, o);
//     end
// endmodule