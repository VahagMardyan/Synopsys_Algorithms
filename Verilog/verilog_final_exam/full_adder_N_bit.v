module full_adder_Nbit #(
    parameter N = 32
)(
    input [N-1:0] a,b,
    input cin,
    output [N-1:0] sum,
    output cout
);
    assign {cout, sum} = a + b + cin;
endmodule

module full_adder_Nbit_tb;
    parameter N = 4;
    reg [N-1:0] a,b;
    reg cin;
    wire [N-1:0] sum;
    wire cout;

    full_adder_Nbit #(.N(N)) dut(.a(a), .b(b), .cin(cin), .sum(sum) ,.cout(cout));

    initial begin
        a = 0; b = 0; cin = 0;

        #10;

        a = 4'b1010;
        b = 4'b0001;
        cin = 0;
        #1;
        $display("a=%b, b=%b, cin=%b, cout=%b, sum=%b", a,b,cin,cout,sum);

        $finish;
    end
endmodule

