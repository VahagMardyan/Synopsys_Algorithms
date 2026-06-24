module sqr (
    input [7:0] d,
    output reg [15:0] Q,
    input clk,
    input rst
);
    reg [7:0] d_reg ;
    wire [15:0] sqr_1;
    assign sqr_1 = d_reg * d_reg;
    always @(posedge clk) begin
        if(!rst)
            d_reg <= 8'd0;
        else
            d_reg <= d;
    end
    always @(posedge clk) begin
        if(!rst)
            Q <= 16'd0;
        else
            Q <= sqr_1;
    end
endmodule