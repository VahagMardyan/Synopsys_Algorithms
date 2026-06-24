module mux_42 (
    input [3:0] d, input [1:0] select, output reg y
);
    always @(*) begin
        case (select)
            2'b00 : y = d[0];
            2'b01 : y = d[1];
            2'b10 : y = d[2];
            2'b11 : y = d[3];
            default: y = 1'bx;
        endcase
    end
endmodule

module mux_42_tb;
    reg [3:0] data;
    reg [1:0] sel;
    wire y;
    mux_42 uut(.d(data), .select(sel), .y(y));

    initial begin
        // $monitor("Time=0%t | data=%b | select=%b | y=%b", $time, data, sel, y);
        data = 4'b0101;
        for(integer i=0; i<4; i = i+1) begin
            sel = i[1:0];
            #10;
        end
        $finish;
    end
    initial begin
        $dumpfile("mux.vcd");
        $dumpvars(0, mux_42_tb);
    end
endmodule