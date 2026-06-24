module xor_3 (
    input a,b,c, output y
);
    assign y = a ^ b ^ c;
endmodule

// module xor_3_tb;
//     reg a,b,c;
//     wire y;
//     xor_3 uut(
//         .a(a), .b(b), .c(c), .y(y)
//     );

//     initial begin
//         for(integer i=0; i<8; i = i+1) begin
//             {a,b,c} = i[2:0];
//             #10;
//         end
//         $finish;
//     end
//     initial begin
//         // $dumpfile("lab2.vcd");
//         // $dumpvars(0, xor_3_tb);
//         $monitor("Time=0%t | a=%b | b=%b | c=%b | y=%b", $time, a,b,c,y);
//     end
// endmodule
