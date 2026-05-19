module piso_shift_register (
    input wire clk,
    input wire rst_n,
    input wire load,               // High to load parallel data
    input wire shift_dir,          // 1 for Right Shift, 0 for Left Shift
    input wire circular,           // 1 for circular shift, 0 for standard
    input wire [7:0] data_in,      // Parallel input data
    output reg [7:0] data_out
);

    always @(posedge clk) begin
        if (!rst_n) begin
            data_out <= 8'b0;
        end else if (load) begin
            data_out <= data_in;
        end else begin
            case ({circular, shift_dir})
                2'b00: data_out <= {data_out[6:0], 1'b0};            // Shift Left (Zero fill)
                2'b01: data_out <= {1'b0, data_out[7:1]};            // Shift Right (Zero fill)
                2'b10: data_out <= {data_out[6:0], data_out[7]};     // Circular Shift Left
                2'b11: data_out <= {data_out[0], data_out[7:1]};     // Circular Shift Right
                default: data_out <= data_out;
            endcase
        end
    end

endmodule
