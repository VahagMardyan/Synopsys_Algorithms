module ring_oscillator (
    output wire osc_out
);

wire w1, w2, w3, w4;
// (* keep = "true" *) wire w1, w2, osc_out;
assign w1 = ~osc_out;
assign w2 = ~w1;
assign w3 = ~w2;
assign w4 = ~w3;
assign osc_out = ~w4;
    
endmodule

`timescale 1ns/1ps

module ring_osc_sim();
    wire out, w1, w2, w3, w4;

    assign #1 w1 = ~out; 
    assign #1 w2 = ~w1; 
    assign #1 w3 = ~w2;
    assign #1 w4 = ~w3;
    assign #1 out = ~w4;

    initial begin
        $dumpfile("./vcd_files/ring_osc_wave.vcd");
        $dumpvars(0, ring_osc_sim);
        $display("Time\t Output");
        $monitor("%0t\t out=%b", $time, out);
        force out = 0;
        #5 release out;
        #100 $finish;
    end
endmodule