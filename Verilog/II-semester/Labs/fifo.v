module fifo #(
   parameter DATA_WIDTH = 8, // can keep up to 2⁸=265 bits data
   parameter ADDR_WIDTH = 4 // there are 2⁴=16 positions
) (
    input clk, rst, wr_en, rd_en,
    input [DATA_WIDTH-1 : 0] data_in,
    output full, empty,
    output reg [DATA_WIDTH - 1 : 0] data_out
);
    reg [DATA_WIDTH : 0] mem [ (1 << ADDR_WIDTH) - 1 : 0];
    reg [ADDR_WIDTH : 0] wr_pt, rd_pt;

    assign empty = (wr_pt == rd_pt);
    assign full = (wr_pt[ADDR_WIDTH - 1 : 0] == rd_pt[ADDR_WIDTH - 1 : 0]) && (wr_pt[ADDR_WIDTH] != rd_pt[ADDR_WIDTH]);

    always @(posedge clk) begin
        if(rst) begin
            wr_pt <= 0;
            rd_pt <= 0;
            data_out <= 0;
        end
        else begin
            if(wr_en && !full) begin
                mem[wr_pt[ADDR_WIDTH - 1 : 0]] <= data_in;
                wr_pt <= wr_pt + 1;
            end

            if(rd_en && !empty) begin
                data_out <= mem[rd_pt[ADDR_WIDTH - 1 : 0]];
                rd_pt <= rd_pt + 1;
            end
        end
    end
endmodule

module fifo_tb;
    parameter DATA_WIDTH = 8;
    parameter ADDR_WIDTH = 2;
    reg clk, rst, wr_en, rd_en;
    reg [DATA_WIDTH - 1 : 0] data_in;
    wire full, empty;
    wire [DATA_WIDTH - 1 : 0] data_out;

    fifo #(.DATA_WIDTH(DATA_WIDTH), .ADDR_WIDTH(ADDR_WIDTH)) uut(
        .clk(clk), .rst(rst), .wr_en(wr_en), .rd_en(rd_en), .data_in(data_in), .full(full), .empty(empty), .data_out(data_out)
    );

    always #5 clk = ~clk;
    integer i;

    initial begin
        $monitor("Time\t=%0t | rst=%b | wr=%b | rd=%b | full=%b | empty=%b | data_in=%d (%b) | data_out=%d (%b)",
            $time, rst, wr_en, rd_en, full, empty, data_in, data_in, data_out, data_out);
    end
    
    initial begin
        clk = 0; rst = 1; wr_en = 0; rd_en = 0; data_in = 0;
        #23 rst = 0;
        for(i=1; i <= (2 << ADDR_WIDTH); i = i+1) begin
            @(negedge clk);
            if(!full) begin
                wr_en = 1;
                data_in = i*2;
            end
        end

        @(negedge clk);
        data_in = 8'd9;

        @(negedge clk);
        wr_en = 0;

        #20;

        while (!empty) begin
            @(negedge clk);
            rd_en = 1;
        end

        @(negedge clk);
        rd_en = 0;
        
        #50 $finish;
    end
    // initial begin
    //     $dumpfile("fifo.vcd");
    //     $dumpvars(0, fifo_tb);
    // end
endmodule