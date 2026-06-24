// Mealy machine
module task_6 (
    in, clk, reset, found
);
    input clk, reset, in;
    output reg found;

    localparam IDLE = 2'b00; // waiting for the first 1
    localparam S1 = 2'b01; // 1
    localparam S10 = 2'b10; // 10
    localparam S101 = 2'b11; // 101

    reg [1:0] state, next_state;

    always @(posedge clk or posedge reset) begin
        if(reset) state <= IDLE;
        else state <= next_state;
    end

    always @(*) begin
        case (state)
           IDLE : next_state = (in == 1) ? S1 : IDLE;
           S1 : next_state = (in == 0) ? S10 : S1;
           S10 : next_state = (in == 1) ? S101 : IDLE; 
           S101 : next_state = (in == 1) ? S1 : S10;
            default: next_state = IDLE;
        endcase
    end

    always @(*) begin
        found = (next_state == S101);
    end

endmodule

module task_6_tb;
    reg clk, reset, in;
    wire found;

    task_6 uut(.clk(clk), .reset(reset), .in(in), .found(found));

    always #5 clk = ~clk;
    initial begin
        clk = 0; reset = 1; in = 0;
        #15; reset = 0;

        $monitor("Time=%0t | reset=%b | in=%b | found=%b", $time, reset, in, found);

        @(posedge clk); in <= 1; // S1
        @(posedge clk); in <= 0; // S10
        @(posedge clk); in <= 1; // S101 -> found should be 1
        @(posedge clk); in <= 0; // S10
        @(posedge clk); in <= 1; // S101 -> found should be 1
        @(posedge clk); in <= 0;
    
    #20 $finish;
    end
endmodule