module tb ();
    reg clk, rst;
    reg [7:0] d;
    reg [15:0] Q;

    sqr sqr1(
        .d(d),
        .clk(clk),
        .rst(rst),
        .Q(Q)
    );

    initial begin
        $monitor("time=%0t | rst=%b | d=%0d | Q=%0d", $time, rst, d, Q);
        clk = 0;
        reset(5);
        repeat(10)
            drive();
        @(posedge clk);
        $finish();
    end

    always 
        #5 clk = ~clk;
    
    task reset(input [4:0] cycle);
        rst = 0;
        repeat(cycle)
            @(posedge clk);
        rst = 1;
    endtask //reset

    task drive();
        d = $random();
        @(posedge clk);
    endtask //drive
endmodule