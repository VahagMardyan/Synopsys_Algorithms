module test;
    reg [7:0] n1;
    initial begin
        // n1 = 16'h4xa;
        // n1 = 6'oz5;
        // n1 = 5'd3;
        n1 = -8'd3;
        $display("%b", n1);
    end
    
endmodule
