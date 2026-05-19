import re

# RTL file to analyze
filename = "rtl/complex.v"

# Read RTL
file = open(filename, "r")
code = file.read()

# Detect operators
operators = re.findall(r'[\+\-\*/&|]', code)

print("\n===== RTL OPTIMIZATION REPORT =====\n")

# Optimization suggestions

if "*" in operators:
    print("Multiplier detected")
    print("Suggestion: Consider pipelining multiplier stage")
    print("Suggestion: Use shift-add architecture if area is critical\n")

if len(operators) >= 2:
    print("Complex combinational logic detected")
    print("Suggestion: Split logic into pipeline stages\n")

if "&" in operators or "|" in operators:
    print("Logic-heavy design detected")
    print("Suggestion: Check logic minimization opportunities\n")

# Detect redundant assignments
if re.search(r'(\w+)\s*<=\s*\1', code):
    print("Redundant self-assignment detected")
    print("Suggestion: Remove unnecessary sequential assignment\n")

print("Optimization analysis completed")

file.close()