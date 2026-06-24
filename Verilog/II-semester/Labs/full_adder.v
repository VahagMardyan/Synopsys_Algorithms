// Full Adder
module adder_n(a, b, c_in, sum, c_out);
    parameter n = 12;
    output [n-1 : 0] sum;
    output c_out;
    input [n-1 : 0] a,b;
    input c_in;

    assign {c_out, sum} = a + b + c_in;
    /*
        wire [n:0] temp_result;
        assign temp_result = a + b + c_in;
        assign sum = temp_result[n-1 : 0];
        assign c_out = temp_result[n];
        // or like this
        assign sum = a + b + c_in;
        assign c_out = ( (a + b + c_in) >> n );
    */
endmodule

module adder_n_tb;
    parameter n = 12;
    reg [n-1 : 0] a,b;
    reg c_in;
    wire [n-1 : 0] sum;
    wire c_out;

    adder_n uut(
        .a(a), .b(b), .c_in(c_in), .sum(sum), .c_out(c_out)
    );
    initial begin
        a = 0; b = 0; c_in = 0;
        $monitor("Time=%0t | a=%d | b=%d | Cin=%b | Sum=%d | Cout=%b", $time, a,b,c_in, sum, c_out);
        #10; a = 12'd100; b=12'd200; c_in=0;
        #10; a = 12'd50; b = 12'd50; c_in = 1;
        #10; a = 12'd500; b = 12'd50; c_in = 0;
        #10;
        $finish;
    end
    initial begin
        $dumpfile("fulladder.vcd");
        $dumpvars(0, adder_n_tb);
    end
endmodule

