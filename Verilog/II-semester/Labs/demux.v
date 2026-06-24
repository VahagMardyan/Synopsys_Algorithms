// 1:4 demux (1 input, 2-bit select and 4 outputs)
module demux_14 (
    in, select, y
);
    input in;
    input [1:0] select;
    output reg [3:0] y;
    always @(*) begin
        y = 4'b0000;
        case (select)
            2'b00 : y[0] = in;
            2'b01 : y[1] = in;
            2'b10 : y[2] = in;
            2'b11 : y[3] = in;
            default: y = 4'b0000;
        endcase
    end
endmodule

// module demux_14_tb;
//     reg in;
//     reg [1:0] select;
//     wire [3:0] y;

//     demux_14 uut(.in(in), .select(select), .y(y));

//     initial begin
//         in = 1;
//         for(integer i=0;i<4; i = i+1) begin
//             select = i[1:0];
//             #10;
//         end
//         $finish;
//     end

//     initial begin
//         // $dumpfile("demux.vcd");
//         // $dumpvars(0, demux_14_tb);
//         $monitor("Time=0%t | in=%b | select=%b | y=%b", $time, in, select, y);
//     end
// endmodule
