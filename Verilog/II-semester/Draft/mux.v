module mux_41 (
    // a0, a1, a2, a3, s, y
    input [3:0] a0, a1, a2, a3,
    input [1:0] s,
    output reg [3:0] y
);

    always @(*) begin
        case (s)
            2'b00 : y = a0;
            2'b01 : y = a1;
            2'b10 : y = a2;
            2'b11 : y = a3;
            default: y = 0;
        endcase
    end
endmodule

module mux_41_tb;
    reg [3:0] a0, a1, a2, a3;
    reg [1:0] s;
    wire [3:0] y;
    integer i;

    mux_41 uut(
        .a0(a0), .a1(a1), .a2(a2), .a3(a3), .s(s), .y(y)
    );

    initial begin
        a0 = 1;
        a1 = 2;
        a2 = 3;
        a3 = 4;
        s = 2'b00;
        for(i=0;i<4;i=i+1) begin
            #5;
            s = i[1:0];
        end
    end
    initial begin
        $monitor("Time=0%t | a0=%b | a1=%b | a2=%b | a3=%b | select=%b | y=%b", $time, a0, a1, a2, a3, s, y);
        $dumpfile("mux.vcd");
        $dumpvars(0, mux_41_tb);
    end
endmodule
