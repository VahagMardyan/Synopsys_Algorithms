module test;
    signed [7:0] number1;
    signed [7:0] number2;

    initial begin
        // Let's assign numbers
        number1 = 5;
        number2 = 6;

        // Operators
        $display("Hello World !");
        $display("Subs ", number1 - number2);
        $display("Add ", number1 + number2);
        $display("And ", number1 & number2);
    end
endmodule
