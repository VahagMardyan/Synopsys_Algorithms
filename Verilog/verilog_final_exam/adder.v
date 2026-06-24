module full_adder_1bit(
    input a, input b, input cin,
    output sum, output cout
);
    assign sum = a ^ b ^ cin;
    assign cout = (a & b) | (cin & (a^b));
endmodule

module full_adder_4bit(
    input [3:0] a,b,
    input cin,
    output [3:0] sum,
    output cout
);

    // Carry-in
    wire c1, c2, c3;

    full_adder_1bit fa0(.a(a[0]), .b(b[0]), .cin(cin), .sum(sum[0]), .cout(c1));
    full_adder_1bit fa1(.a(a[1]), .b(b[1]), .cin(c1), .sum(sum[1]), .cout(c2));
    full_adder_1bit fa2(.a(a[2]), .b(b[2]), .cin(c2), .sum(sum[2]), .cout(c3));
    full_adder_1bit fa3(.a(a[3]), .b(b[3]), .cin(c3), .sum(sum[3]), .cout(cout));

endmodule

module full_adder_4bit_tb;
    reg [3:0] a,b;
    reg cin;
    wire [3:0] sum;
    wire cout;

    full_adder_4bit dut(.a(a), .b(b), .cin(cin), .sum(sum), .cout(cout));

    initial begin
        a = 4'b1010; b = 4'b0010; cin = 0;
        #2;
        $display("a=%b | b=%b | cin=%b | cout=%b | sum=%b", a,b,cin,cout,sum);
    end
endmodule

