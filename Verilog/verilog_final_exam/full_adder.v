module full_adder_4bit(
    input [3:0] a, b,
    input cin,
    output [3:0] sum,
    output cout
);  
    // // {cout, sum}-ը 5 բիթանոց վեկտոր է, որը պարունակում է գումարը և գերլցումը:
    assign {cout, sum} = a + b + cin;
endmodule

module full_adder_4bit_tb;
    reg [3:0] a,b;
    reg cin;
    wire [3:0] sum;
    wire cout;

    full_adder_4bit dut(.a(a), .b(b), .cin(cin), .sum(sum), .cout(cout));

    initial begin
        a = 0; b = 0; cin = 0;
        
        #10;

        a = 4'b1010;
        b = 4'b0001;
        cin = 0;
        #1;
        $display("a=%b, b=%b, cin=%b, cout=%b, sum=%b", a,b,cin,cout,sum);

        #10;
        a = 4'b1111;
        b = 4'b0001;
        cin = 0;
        #1;
        $display("a=%b, b=%b, cin=%b, cout=%b, sum=%b", a,b,cin,cout,sum);

        #10;
        a = 4'b1010;
        b = 4'b1011;
        cin = 1;
        #1;
        $display("a=%b, b=%b, cin=%b, cout=%b, sum=%b", a,b,cin,cout,sum);

        $finish;
    end
endmodule
