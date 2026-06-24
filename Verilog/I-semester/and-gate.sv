module and_gate(
    input a,b,c,d,
    output y
);
    assign y = a & b & c & d;
endmodule

module test_and ();
    reg a,b,c,d;
    wire y;
    and_gate dut(a,b,c,d,y);
    initial begin
        $dumpfile("./vcd_files/and_wave.vcd");
        $dumpvars(0, test_and);
        for(int i=0;i<16;i++) begin
            {a,b,c,d} = i[3:0];
            #5;
            $display("a=%b b=%b c=%b d=%b y=%b",a,b,c,d,y);
        end
    end
    
endmodule