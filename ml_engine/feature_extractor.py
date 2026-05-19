import re
import csv

# Select RTL file
filename = "rtl/complex.v"
# Read RTL code
file = open(filename, "r")
code = file.read()

# Extract features
adders = code.count("+")
multipliers = code.count("*")
ands = code.count("&")
ors = code.count("|")

always_blocks = len(re.findall(r'always', code))

inputs = len(re.findall(r'input', code))
outputs = len(re.findall(r'output', code))

# Store features
features = [
    adders,
    multipliers,
    ands,
    ors,
    always_blocks,
    inputs,
    outputs
]

# CSV header
header = [
    "adders",
    "multipliers",
    "ands",
    "ors",
    "always_blocks",
    "inputs",
    "outputs"
]

# Save to CSV
with open("datasets/rtl_features.csv", "w", newline="") as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow(header)
    writer.writerow(features)

print("\nFeatures saved to CSV successfully")

file.close()