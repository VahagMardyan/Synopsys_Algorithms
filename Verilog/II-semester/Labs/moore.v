// Moore machine
// 00011 (posedge clk, posedge set)

module moore(x, set, clk, y);
    input x, clk, set;
    output reg y;
    parameter s0 = 3'b000; // start
    parameter s1 = 3'b001; // 0
    parameter s2 = 3'b010; // 00
    parameter s3 = 3'b011; // 000
    parameter s4 = 3'b100; // 0001
    parameter s5 = 3'b101; // 00011
 
    reg [2:0] current_state, next_state;

    always @(posedge clk or posedge set) begin
        if(set) 
            current_state <= s0;
        else
            current_state <= next_state;
    end

    always @(*) begin
        case (current_state)
            s0 : next_state = (x == 1'b0) ? s1 : s0;
            s1 : next_state = (x == 1'b0) ? s2 : s0;
            s2 : next_state = (x == 1'b0) ? s3 : s0;
            s3 : next_state = (x == 1'b1) ? s4 : s3;
            s4 : next_state = (x == 1'b1) ? s5 : s1;
            // overlap
            s5 : next_state = (x == 1'b0) ? s1 : s0;
            default: next_state = s0;
        endcase
    end
    always @(*) begin
        y = (current_state == s5);
    end
endmodule

module moore_tb;
    reg x, set, clk;
    wire y;
    moore uut(
        .x(x), .set(set), .clk(clk), .y(y)
    );

    always #5 clk = ~clk;
    
    initial begin
        clk = 0;
        set = 1;
        x = 0;
        #12 set = 0;

        @(negedge clk) x = 0;
        @(negedge clk) x = 0;
        @(negedge clk) x = 0;
        @(negedge clk) x = 1;
        @(negedge clk) x = 1;

        @(negedge clk) x = 0;

        #30;
        $display("Simulation is done");
        $finish;
    end
    initial begin
        $dumpfile("lab4.vcd");
        $dumpvars(0, moore_tb);
        $monitor("Time=%0t | x=%b | state = %b | y=%b | set=%b", $time, x, uut.current_state, y, set);
    end
endmodule