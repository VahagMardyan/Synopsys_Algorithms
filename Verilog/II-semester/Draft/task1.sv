module test;
    reg [7:0] number1;
    reg [7:0] number2;

    initial begin
        number1 = 3'b000;
        number2 = 4'b0001;
        $display("Subs = %d", number1 - number2);
        $display("Add  = %d", number1 + number2);
        $display("And  = %d", number1 & number2);
        $display("Div  = %d", number1 / number2);
    end
endmodule

// class Packet;
//     int addr;
//     int data;

//     function void display();
//         $display("addr=%0d data=%0d", addr, data);
//     endfunction
// endclass

// module test;
//     initial begin
//         Packet p = new();
//         p.addr = 5;
//         p.data = 10;
//         p.display();
//     end
// endmodule