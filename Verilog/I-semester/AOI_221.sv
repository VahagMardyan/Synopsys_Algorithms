module AOI221 (
    input a,b,c,d,e,
    output y
);
    assign y=~(a&b | c&d | e);
endmodule

module test_aoi ();
    reg a,b,c,d,e;
    wire y;
    AOI221 dut(a,b,c,d,e,y);
    initial begin
        for(int i=0;i<32;i++) begin
            {a,b,c,d,e} = i[4:0];
            #5;
            $display("In1=%b | In2=%b | In3=%b | In4=%b | In5=%b | Out=%b",a,b,c,d,e,y);
        end
    end
endmodule
