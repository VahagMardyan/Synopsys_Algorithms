module OAOI211 (
    input a,b,c,d,
    output y
);
    assign y = ~( (a & b) | c | d);
endmodule

module test_oaoi ();
    reg a,b,c,d;
    wire y;
    OAOI211 dut(a,b,c,d,y);
    initial begin
        for(int i=0;i<16;i++) begin
            {a,b,c,d} = i[3:0];
            #5;
            $display("a=%b b=%b c=%b d=%b y=%b",a,b,c,d,y);
        end
    end
    
endmodule