// module mux_4_to_1_dataflow(
//     input [3:0] in, input [1:0] sel, output out
// );
//     assign out = (sel == 2'b00) ? in[0] :
//                 (sel == 2'b01) ? in[1] :
//                 (sel == 2'b10) ? in[2] : in[3];
//     // // կամ 
//     // assign out = in[sel];
// endmodule

// module mux_4_to_1_behavioral(
//     input [3:0] in, input [1:0] sel, output reg out
// );
//     always @(*) begin
//         case (sel)
//             2'b00: out = in[0];
//             2'b01: out = in[1];
//             2'b10: out = in[2];
//             2'b11: out = in[3];
//             default: out = 1'bx;
//         endcase
//     end
// endmodule

// module mux_4_to_1_gate(
//     input [3:0] in, input [1:0] sel, output out
// );
//     wire not_s1, not_s0, w0, w1, w2, w3;
    
//     not (not_s1, sel[1]);
//     not (not_s0, sel[0]);

//     and (w0, in[0], not_s1, not_s0);
//     and (w1, in[1], not_s1, sel[0]);
//     and (w2, in[2], sel[1], not_s0);
//     and (w3, in[3], sel[1], sel[0]);

//     or (out, w0, w1, w2, w3);
// endmodule

module mux_tb;
    reg [3:0] in;
    reg [1:0] sel;
    wire out;

    mux_4_to_1_gate dut(.in(in), .sel(sel), .out(out));
    // mux_4_to_1_behavioral dut();
    // mux_4_to_1_dataflow dut(.in(in), .sel(sel), .out(out));
    initial begin
        in = 4'b0101;
        for(integer i=0; i < 4; i = i + 1) begin
          sel = i[1:0];
            #5;
            $display("in=%b | sel=%b | out=%b", in, sel, out);
        end
        
    end

endmodule