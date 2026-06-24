module comparator (
    A, B, A_greater_B, A_equal_B, A_less_B
);
    parameter n = 8;
    input [n-1 : 0] A, B;
    output reg A_greater_B, A_equal_B, A_less_B;

    always @(*) begin
        A_greater_B = 0;
        A_equal_B = 0;
        A_less_B = 0;

        if (A > B) A_greater_B = 1;
        else if (A == B) A_equal_B = 1;
        else A_less_B = 1;
    end
endmodule

// `ifndef SYNTHESIS 
module comparator_tb;
    parameter n = 8;
    reg [n-1 : 0] A, B;
    wire A_greater_B, A_equal_B, A_less_B;
    comparator uut(
        .A(A), .B(B), .A_greater_B(A_greater_B), .A_equal_B(A_equal_B), .A_less_B(A_less_B)
    );
    initial begin
        $monitor("Time=%0t | A=%d | B=%d | A>B: %b | A=B: %b | A<B: %b", $time, A, B, A_greater_B, A_equal_B, A_less_B);

        A = 0; B = 0;
        #10;
        A = 5; B = 10; 
        #10;
        A = 8; B = 3;
        #10;
        A = 7; B = 7;
        #10;
        $finish;
    end
    // initial begin
    //     $dumpfile("comparator.vcd");
    //     $dumpvars(0, comparator_tb);
    // end
endmodule
// `endif