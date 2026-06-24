module memory(
    cs, addr, data_in, data_out, re
);

    /*
        cs -> chip select; if cs = 0 then memory is disabled
        re -> write / read enable
        IF re is 1 -> read ELSE write
    */

    input cs, re;
    input [7:0] data_in;
    input [5:0] addr;
    output reg [7:0] data_out;
    reg [7:0] mem[0:63];

    always @(data_in or cs or addr or re) begin
        if(cs) begin
            // write operation
            if(!re)
                mem[addr] = data_in;
            // read operation
            else
                data_out = mem[addr];
        end
        else
            data_out = 8'bzz;
    end
endmodule

module memory_tb;
    reg cs, re;
    reg [7:0] data_in;
    reg [5:0] addr;
    wire [7:0] data_out;

    memory uut(
        .cs(cs), .addr(addr), .data_in(data_in), .data_out(data_out), .re(re)
    );

    initial begin
        cs = 0; re = 0; addr = 0; data_in = 0;

        $monitor("Time=%0t | CS=%b re=%b ADDR=%d | IN=%h | OUT=%h", $time, cs, re, addr, data_in, data_out);

        #10;

        // Write to address 10
        cs = 1; re = 0; addr = 6'd10; data_in = 8'hA5;
        #10;

        // write to address 55
        cs = 1; re = 0; addr = 6'd55; data_in = 8'h3C;
        #10;

        // read from address 10
        re = 1; addr = 6'd10;
        #10;

        // read from address 55 (re is 1)
        addr = 6'd55;
        #10;

        // deselect chip
        cs = 0;
        #10;

        // read from address 10 while CS is 0
        cs = 0; re = 1; addr = 6'd10;
        #10;

        $finish;
    end

    initial begin
        $dumpfile("s_memory.vcd");
        $dumpvars(0, memory_tb);
    end
endmodule
