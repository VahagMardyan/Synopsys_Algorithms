module dff (
    input clk, rst, d, output q
);
    reg q;
    always @(posedge clk) begin
        if(!rst)
            q <= 1'b0;
        else
            q <= d;
    end
endmodule

module dff_tb();
    reg clk;
    reg rst;
    reg d;
    wire q;
    dff dut(.clk(clk), .rst(rst), .d(d), .q(q));
    always #5 clk = ~clk;
    initial begin
        clk = 0;
        rst = 0;
        d = 0;
        $display("Time\t clk rst d | q");
        $display("-----------------------");
        #15;
        rst = 1;
        d = 1;
        #10;

        d = 0;
        #10;

        d = 1;
        #3;
        d = 0;
        #2;
        d = 1;
        #15;
        rst = 0;
        #10;
        $finish;
    end
    initial begin
        $dumpfile("dff.vcd");
        $dumpvars(0, dff_tb);
        $monitor("%0t\t %b %b %b | %b", $time, clk, rst, d, q);
    end
endmodule