module complex(
    input [7:0] a,
    input [7:0] b,
    input [7:0] c,
    output [15:0] y
);

assign y = (a * b) + c;

endmodule