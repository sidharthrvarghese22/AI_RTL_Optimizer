import re

# Open RTL file
filename = "rtl/bad_design.v"

file = open(filename, "r")
code = file.read()

# Detect operators
operators = re.findall(r'[\+\-\*/&|]', code)

# Count operations
operation_count = len(operators)

print("Operators Found:", operators)
print("Operation Count:", operation_count)

# Timing analysis
if operation_count >= 2:
    print("WARNING: Possible timing-critical combinational path")

# Area analysis
if "*" in operators:
    print("WARNING: Multiplier may increase chip area")

# Power analysis
if operation_count > 3:
    print("WARNING: High switching activity possible")
    
if re.search(r'(\w+)\s*<=\s*\1', code):
    print("WARNING: Redundant self-assignment detected")

file.close()