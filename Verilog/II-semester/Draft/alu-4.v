module alu (
    a,b, opcode, result, zero
);
    input [3:0] a,b;
    input [2:0] opcode;
    output reg [3:0] result;
    output reg zero;

    always @(*) begin
        case (opcode)
            3'b000 : result = a + b;
            3'b001 : result = a - b;
            3'b010 : result = a & b;
            3'b011 : result = a | b;
            3'b100 : result = a ^ b;
            3'b101 : result = a << 1;
            3'b110 : result = a >> 1;
            3'b111 : result = (a == b) ? 4'b0001 : 4'b0000;
            default: result = 4'b000;
        endcase
        zero = (result == 4'b0000);
    end
endmodule

module alu_tb();
    reg [3:0] a,b;
    reg [2:0] opcode;
    wire [3:0] result;
    wire zero;

    alu uut(
        .a(a), .b(b), .opcode(opcode), .result(result), .zero(zero)
    );

    integer i;
    initial begin
    a = 5;
    b = 4;
        for(i=0; i<8; i = i+1) begin
            opcode = i[2:0];
            #10;
        end
        #10;
        $finish;
    end

    initial begin
        $dumpfile("alu.vcd");
        $dumpvars(0, alu_tb);
        $monitor("Time=0%t | a=%d | b=%d | opcode=%b | result=%d | zero=%b", $time, a, b, opcode, result, zero);
    end
endmodule
