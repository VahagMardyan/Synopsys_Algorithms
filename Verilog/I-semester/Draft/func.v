module f1(input a, b, c, output y);
    assign y=b | ((~a) & (~c));
endmodule

// [0:0] -> 1bit starts from 0 ends with 0 w