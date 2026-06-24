module seq_det (
    x,y,clk,reset
);
    input x, clk, reset;
    output reg y;
    parameter s0 = 3'b000; // start
    parameter s1 = 3'b001; // 0
    parameter s2 = 3'b010; // 01
    parameter s3 = 3'b011; // 010
    parameter s4 = 3'b100; // 0101
    parameter s5 = 3'b101; // 01010
    parameter s6 = 3'b110; // 010100
    parameter s7 = 3'b111; // 0101001

    reg [2:0] current_state, next_state;

    always @(posedge clk or negedge reset) begin
        // if(!reset) begin
        //     current_state <= s0;
        // end
        // else begin
        //     current_state <= next_state;
        // end
        current_state <= (!reset) ? s0 : next_state;
    end

    always @(*) begin
        case (current_state)
            s0 : next_state = (x == 1'b0) ? s1 : s0;
            s1 : next_state = (x == 1'b1) ? s2 : s1;
            s2 : next_state = (x == 1'b0) ? s3 : s0;
            s3 : next_state = (x == 1'b1) ? s4 : s1;
            s4 : next_state = (x == 1'b0) ? s5 : s0;
            s5 : next_state = (x == 1'b0) ? s6 : s4;
            s6 : next_state = (x == 1'b1) ? s7 : s1;

            // Data overlap
            s7 : next_state = (x == 1'b0) ? s3 : s0; // s2 instead of s1
            default: next_state = s0;
        endcase
    end

    always @(*) begin
        y = (current_state == s7);
    end    
endmodule

module tb();
    reg x, clk, reset;
    wire y;

    seq_det uut(
        .x(x),
        .clk(clk),
        .reset(reset),
        .y(y)
    );

    always #5 clk = ~clk;

    initial begin
        clk = 0;
        reset = 0;
        x = 0;

        #12 reset = 1;
        
        @(negedge clk) x = 0;
        @(negedge clk) x = 1;
        @(negedge clk) x = 0;   
        @(negedge clk) x = 1;   
        @(negedge clk) x = 0;   
        @(negedge clk) x = 0;   
        @(negedge clk) x = 1;

        @(negedge clk) x = 0;   
        @(negedge clk) x = 0;
        
        #50;
        $display("Simulation is done");
        $finish;   
    end

    initial begin
        $monitor("Time=%0t | x=%b | state = %b | y=%b", $time, x, uut.current_state, y);
        $dumpfile("moore.vcd");
        $dumpvars(0, tb);
    end
endmodule