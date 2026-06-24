module task_3 (
    a,b, cin, sum, cout
);
    input [3:0] a,b;
    input cin;
    output [3:0] sum;
    output cout;
    // {cout sum} becames a 5-bit vector
    assign {cout, sum} = a + b + cin;
endmodule

module task_3_tb;
    reg [3:0] a , b;
    reg cin;
    
    wire [3:0] sum;
    wire cout;

    task_3 uut (
        .a(a), .b(b), .cin(cin), .sum(sum), .cout(cout)
    );

    initial begin
        $monitor("Time=%0t | a=%b | b=%b | c_in=%b | sum=%b | c_out=%b", $time, a, b, cin, sum, cout);

        a = 0; b = 0; cin = 0; #10;

        a = 4'b0011; b = 4'b1111; cin = 0; #10;
        
        a = 4'b1000; b = 4'b0010; cin = 0; #10;

        $finish;
    end
endmodule