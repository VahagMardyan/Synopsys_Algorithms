module demux_42 (
    input d, input [1:0] select, output reg [3:0] y
);
    always @(*) begin
        y = 4'b0000;
        case (select)
            2'b00 : y[0] = d;
            2'b01 : y[1] = d;
            2'b10 : y[2] = d;
            2'b11 : y[3] = d;
            default: y = 4'bz;
        endcase
    end
endmodule

module demux_42_tb;
    reg data;
    reg [1:0] sel;
    wire [3:0] y;
    demux_42 uut(.d(data), .select(sel), .y(y));
    initial begin
        $monitor("Time=%0t | data=%b | select=%b | y=%b", $time, data, sel, y);
        data = 1;
        for(integer i=0; i < 4; i = i+1) begin
            sel = i[1:0];
            #10;
        end
        $finish;
    end
endmodule