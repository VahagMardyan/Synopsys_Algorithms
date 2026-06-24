module compare(
    signal1, signal2, compout
);
    output compout;
    input [31:0] signal1, signal2;
    assign compout = (signal1 == signal2);
endmodule

module compare_tb;
    reg [31:0] signal1, signal2;
    wire compout;
    compare uut(.signal1(signal1), .signal2(signal2), .compout(compout));

    initial begin
        $monitor("Time=%0t | sig1=%d | sig2=%d | sig1==sig2: %b", $time, signal1, signal2, compout);
        signal1 = 18; signal2 = 18;
        #10;
        signal1 = 25; signal2 = 21;
        #10;
        signal1 = 29; signal2 = 29;
        #10;
        $finish;
    end
endmodule
