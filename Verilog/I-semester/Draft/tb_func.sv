module tb;
    reg a,b,c;
    wire y;
    f1 uut(.a(a), .b(b), .c(c), .y(y));

    initial begin
        $monitor("a=%b b=%b c=%b y=%b", a,b,c, y);
        for(integer i=0; i<8; i=i+1) begin
            {a,b,c} = i[2:0];
            #10;
        end

    // $finish;
    end
endmodule
