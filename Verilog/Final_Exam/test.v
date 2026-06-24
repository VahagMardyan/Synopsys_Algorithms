module sequence_detector_010001(
    input clk,
    input rst,
    input din,
    output reg match
);
    // Վիճակների կոդավորում (Binary)
    localparam S0 = 3'd0, // Սկզբնական վիճակ
               S1 = 3'd1, // Ստացվել է "0"
               S2 = 3'd2, // Ստացվել է "01"
               S3 = 3'd3, // Ստացվել է "010"
               S4 = 3'd4, // Ստացվել է "0100"
               S5 = 3'd5; // Ստացվել է "01000"

    reg [2:0] current_state, next_state;

    // Վիճակի հիշողություն (Sequential բլոկ)
    always @(posedge clk or posedge rst) begin
        if (rst) current_state <= S0;
        else     current_state <= next_state;
    end

    // Հաջորդ վիճակի և ելքի որոշում (Combinational բլոկ)
    always @(*) begin
        // Նախնական արժեքներ
        next_state = current_state;
        match = 1'b0;

        case (current_state)
            S0: if (din == 0) next_state = S1; else next_state = S0;
            S1: if (din == 1) next_state = S2; else next_state = S1;
            S2: if (din == 0) next_state = S3; else next_state = S0;
            S3: if (din == 0) next_state = S4; else next_state = S2;
            S4: if (din == 0) next_state = S5; else next_state = S2;
            S5: begin
                if (din == 1) begin
                    next_state = S2; // "010001" հայտնաբերվեց, նոր հաջորդականությունը կարող է սկսվել "01"-ից (overlapping)
                    match = 1'b1;
                end else begin
                    next_state = S1;
                end
            end
            default: next_state = S0;
        endcase
    end
endmodule