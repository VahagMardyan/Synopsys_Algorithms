module counter_n #(parameter n=8) (clk, reset, count);
    input clk;
    input reset;
    output reg [n-1 : 0] count;
    always @(posedge clk or posedge reset) begin
        if(reset) count <= 0;
        else count <= count + 1;
    end
endmodule

module counter_n_tb;
    parameter n = 8;
    reg clk, reset;
    wire [n-1:0] count;

    counter_n #(.n(n)) uut (
        .clk(clk), .reset(reset), .count(count)
    );

    always #5 clk = ~clk;

    initial begin
        $monitor("Time=%0t | Reset=%b | Count=%d (%b)", $time, reset, count, count);
        clk = 0;
        reset = 1; // reset on
        #15;
        reset = 0; // reset off

        #99;

        $finish;
    end

    // initial begin
    //     $dumpfile("counter.vcd");
    //     $dumpvars(0, counter_n_tb);
    // end
endmodule