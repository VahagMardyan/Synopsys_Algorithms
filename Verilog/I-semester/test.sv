module test (
    input a,b,
    output y
);
    assign y=~(a & b);
endmodule

module test_module ();
    reg a,b;
    wire y;
    test dut(a,b,y);
    initial begin
        for(int i=0;i<4;i++) begin
            {a,b} = i[2:0];
            #5;
            $display("In1=%b | In2=%b | Out=%b",a,b,y);
        end
    end
endmodule
