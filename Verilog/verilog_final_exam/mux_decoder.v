module mux_2to1_behavioral(input a, input b, input sel, output reg y);
    always @(*) begin
        if(sel == 1'b1) begin
            y = b;
        end
        else begin
            y = a;
        end
    end
endmodule

// module mux_2to1_dataflow(input a, input b, input sel, output y);
//     assign y = sel == 1'b1 ? b : a;
// endmodule

// module mux_2to1_gate(input a, input b, input sel, output y);
//     wire sel_n, w1, w2;
//     not u1(sel_n, sel); // sel_n = ~sel
//     and u2(w1, a, sel_n); // w1 = a & ~sel
//     and u3(w2, b, sel); // w2 = b & sel
//     or u4(y, w1, w2); // y = w1 | w2
// endmodule

module mux_tb;
    reg a,b,sel;
    wire y;
    mux_2to1_gate dut(.a(a), .b(b), .sel(sel), .y(y));
    // mux_2to1_dataflow dut(.a(a), .b(b), .sel(sel), .y(y));
    // mux_2to1_behavioral dut(.a(a), .b(b), .sel(sel), .y(y));

    initial begin
        a = 0;
        b = 1;
        for(integer i=0;i<2;i=i+1) begin
          sel = i;
          #5;
          $display("a=%b | b=%b | sel=%b | y=%b",a,b,sel,y);
        end
        $finish;
    end 
endmodule

//////////////////////////////////////////////////////////////////

// module decoder2to4_behavioral(input [1:0] in, output reg [3:0] out);
//     always @(*) begin
//         case (in)
//            2'b00 : out = 4'b0001;
//            2'b01 : out = 4'b0010;
//            2'b10 : out = 4'b0100;
//            2'b11 : out = 4'b1000;
//            default: out = 4'b0000;
//         endcase
//     end
// endmodule

// module decoder2to4_dataflow(input [1:0] in, output [3:0] out);
//     assign out = 4'b0001 << in;
// endmodule

// module decoder2to4_gate(input [1:0] in, output [3:0] out);
//     wire in0_n, in1_n;

//     not u0(in0_n, in[0]);
//     not u1(in1_n, in[1]);

//     and g0(out[0], in1_n, in0_n); // out[0] = ~in[1] & ~in[0] (00)
//     and g1(out[1], in1_n, in[0]); // out[1] = ~in[1] & in[0] (01)
//     and g2(out[2], in[1], in0_n); // out[2] = in[1] & ~in[0] (10)
//     and g3(out[3], in[1], in[0]); // out[3] = in[1] & in[0] (11)
// endmodule

module decoder_tb;
    reg [1:0] in;
    wire [3:0] out;
    decoder2to4_gate dut(.in(in), .out(out));
    // decoder2to4_dataflow dut(.in(in), .out(out));
    // decoder2to4_behavioral dut(.in(in), .out(out));

    initial begin
        for(integer i=0;i<4;i = i + 1) begin
            in = i[3:0];
            #5;
            $display("in=%b | out=%b", in, out);
        end
        $finish;
    end
endmodule