module moore_machine (
    x, set, clk, y
);
    input x, clk, set;
    output reg y;

    parameter s0 = 3'b000; // start
    parameter s1 = 3'b001; // 1
    parameter s2 = 3'b010; // 10
    parameter s3 = 3'b011; // 100
    parameter s4 = 3'b100; // 1001
    parameter s5 = 3'b101; // 10010
    parameter s6 = 3'b110; // 100101

    reg [2:0] current_state, next_state;

    always @(negedge clk or posedge set) begin
        if(set) begin
            current_state <= s0;
        end
        else begin
            current_state <= next_state;
        end
    end

    always @(*) begin
        case (current_state)
            s0 : next_state = (x == 1'b1) ? s1 : s0;
            s1 : next_state = (x == 1'b0) ? s2 : s1;
            s2 : next_state = (x == 1'b0) ? s3 : s1;
            s3 : next_state = (x == 1'b1) ? s4 : s0;
            s4 : next_state = (x == 1'b0) ? s5 : s1;
            s5 : next_state = (x == 1'b1) ? s6 : s3;

            // data overlap
            s6 : next_state = (x == 1'b0) ? s2 : s1;

            default: next_state = s0;
        endcase
    end

    always @(*) begin
        y = (current_state == s6);
    end
endmodule

module moore_machine_tb ();
    reg x, clk, set;
    wire y;

    moore_machine uut(.x(x), .clk(clk), .set(set), .y(y));

    always #5 clk = ~clk;

    initial begin
        clk = 0;
        set = 0;
        x = 0;
        
        #8 set = 1;
        #13 set = 0;

        @(negedge clk) x = 1;
        @(negedge clk) x = 0;
        @(negedge clk) x = 0;
        @(negedge clk) x = 1;
        @(negedge clk) x = 0;
        @(negedge clk) x = 1;

        #20;
        $display("Done");
        $finish;
    end
    initial begin
        $monitor("Time=%0t | x=%b | state=%b | set=%b | y=%b", $time, x, uut.current_state, set, y);
        $dumpfile("moore1");
        $dumpvars(0, moore_machine_tb);
    end
endmodule