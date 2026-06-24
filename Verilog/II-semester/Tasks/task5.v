module task_4 #(parameter n = 4) (
    clk, en, reset, up_down, count
);
    input clk, reset, en, up_down;
    output reg signed [n-1:0] count;

    always @(posedge clk or posedge reset) begin
        if(reset) begin
            count <= 0;
        end
        else if(en) begin
            if(up_down) 
                count <= count + 1;
            else
                count <= count - 1;
        end
    end
endmodule

module task_4_tb;
    parameter n = 4;
    reg clk, reset, en, up_down;
    wire signed [n-1 : 0] count;
    task_4 #(.n(n)) uut(.clk(clk), .reset(reset), .en(en), .up_down(up_down), .count(count));

    always #5 clk = ~clk;
    always #20 up_down = ~up_down;

    initial begin
        $monitor("Time=%0t | reset=%b | enable=%b | count=%d (%b)", $time, reset, en, count, count);

        clk = 0;
        reset = 1; // reset on
        en = 0;
        up_down = 0;
        #15;
        reset = 0; // reset off

        en = 1;
        #4;
        en = 1;
        #99;
        $finish;
    end
endmodule