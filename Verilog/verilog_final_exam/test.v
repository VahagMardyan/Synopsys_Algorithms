module mux2to1(input a, b, sel, output y);
    wire not_sel, w1, w2;
    not u1(not_sel, sel);
    and u2(w1, a, not_sel);
    and u3(w2, b, sel);
    or u4(y, w1, w2);
endmodule

