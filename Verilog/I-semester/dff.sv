module dff (
    input wire d,
    input wire clk,
    output reg q
);
    always @(posedge clk) begin
        q <= d;
    end
    
endmodule

`timescale 1ns/1ns

module tb_dff();
    reg d;
    reg clk;
    wire q;
    dff uut(
        .d(d),
        .clk(clk),
        .q(q)
    );
    initial begin
        clk = 0;
        forever #5 clk = ~clk;
    end
    initial begin
    $dumpfile("./vcd_files/dff_wave.vcd"); // Ստեղծում է ֆայլը, որտեղ պահվելու են գրաֆիկները
    $dumpvars(0, tb_dff);      // Ասում է՝ պահիր tb_dff-ի բոլոր լարերի փոփոխությունները
    
    $display("Time\t clk\t data\t q");
    $monitor("%0t\t %b\t %b\t %b", $time, clk, d, q);

    d = 0;
    #7 d = 1;
    #10 d = 0;
    #10 d = 1;
    #20 $finish;
end
endmodule