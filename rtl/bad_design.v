module bad_design(
    input clk,
    input enable,
    input [7:0] a,
    output reg [7:0] y
);

always @(posedge clk)
begin
    if(enable)
        y <= a;
    else
        y <= y;
end

endmodule