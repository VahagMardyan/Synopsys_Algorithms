// Carry Look-Ahead Adder
module cla_adder(a, b, c_in, sum);

    parameter n = 8;
    input [n-1:0] a,b;
    input c_in;

    output [n:0] sum;

    reg [n:0] sum;
    reg [n:0] carry;
    reg [n-1:0] index, shift;

    integer i;

    always @(a or b or c_in) begin
        carry[0] = c_in;
        for(i=0;i<n;i=i+1) begin
            index[i] = a[i] & b[i]; // Generate: G[i]
            shift[i] = a[i] ^ b[i]; // Propogate: P[i]
            carry[i+1] = index[i] | (shift[i] & carry[i]); // G[i] | (P[i] & carry[i])
            sum[i] = shift[i] ^ carry[i]; // P[i] ^ carry[i]
        end
        sum[n] = carry[n];
    end
endmodule

module cla_adder_tb;
    parameter n = 8;
    reg [n-1:0] a,b;
    reg c_in;

    wire [n:0] sum;

    cla_adder uut(
        .a(a), .b(b), .c_in(c_in), .sum(sum)
    );

    initial begin
        a = 0; b = 0; c_in = 0;
        $monitor("Time=0%t | a=%d | b=%d | Cin=%b | Sum=%d (Hex:%h)", $time, a, b, c_in, sum, sum);
        
        #10; a = 8'd10; b = 8'd20; c_in = 0;

        #10; a = 8'hFF; b = 8'hFF; c_in = 1;
        
        #10;
        $finish;
    end

    // initial begin
    //     $dumpfile("cla_adder.vcd");
    //     $dumpvars(0, cla_adder_tb);
    // end
endmodule
