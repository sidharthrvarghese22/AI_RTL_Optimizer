import re

# Open RTL file
filename = "rtl/complex.v"

file = open(filename, "r")

# Read entire code
code = file.read()

# Extract module name
module = re.search(r'module\s+(\w+)', code)

# Extract inputs
inputs = re.findall(r'input\s+(?:\[\d+:\d+\]\s+)?(\w+)', code)

# Extract outputs
outputs = re.findall(r'output\s+(?:\[\d+:\d+\]\s+)?(\w+)', code)

# Print results
print("Module Name:", module.group(1))
print("Inputs:", inputs)
print("Outputs:", outputs)
operators = re.findall(r'[\+\-\*/&|]', code)
print("Operators:", operators)
print("Number of Operations:", len(operators))
if "*" in operators:
    print("WARNING: Multiplier detected")

if len(operators) > 2:
    print("WARNING: Complex combinational logic")
file.close()