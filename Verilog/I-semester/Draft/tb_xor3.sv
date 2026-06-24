module func (input a,b,c,d, output y);
  assign y = ~( (a&b) | (c&d) );
endmodule

module tb;
    reg a,b,c,d;
    wire y;

    func uut(.a(a), .b(b), .c(c), .d(d), .y(y));

    initial begin
      $monitor("a=%b b=%b c=%b d=%b y=%b", a,b,c,d, y);
      for(integer i=0; i<16; i=i+1) begin
        {a,b,c,d} = i[3:0];
        #10;
      end
      
      $finish;
    end
endmodule
