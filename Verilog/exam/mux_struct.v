module mux_41_struct(
    input [3:0] d,
    input [1:0] sel,
    output y
);

    // // y = !s1*!s0*d0 + !s1*s0*d1 + s1*!s0*d2 + s1*s0*d3;

    wire s1_n, s0_n; // Inverse selectors
    wire w0, w1, w2, w3;

    not n1(s1_n, sel[1]);
    not n2(s0_n, sel[0]);

    and a0(w0, d[0], s1_n, s0_n); // 00
    and a1(w1, d[1], s1_n, sel[0]); // 01
    and a2(w2, d[2], sel[1], s0_n); // 10
    and a3(w3, d[3], sel[1], sel[0]); // 11

    or out(y, w0, w1, w2, w3);
endmodule

module mux_41_struct_tb;
    reg [3:0] data;
    reg [1:0] select;
    wire y;
    mux_41_struct uut(.d(data), .sel(select), .y(y));

    initial begin
        $monitor("Time=%0t | data=%b | select=%b | y=%b", $time, data, select, y);
        data = 4'b1101;
        for(integer i=0; i<4; i = i + 1) begin
          select = i[1:0];
          #10;
        end
        #16 $finish;
    end
endmodule