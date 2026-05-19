import os

print("\n========== AI RTL OPTIMIZER ==========\n")

print("1. RTL Parser")
print("2. RTL Analyzer")
print("3. Feature Extractor")
print("4. Optimization Engine")
print("5. ML Delay Predictor")

choice = input("\nEnter your choice: ")

# Parser
if choice == "1":
    os.system("python3 parser/rtl_parser.py")

# Analyzer
elif choice == "2":
    os.system("python3 analyzer/rtl_analyzer.py")

# Feature Extractor
elif choice == "3":
    os.system("python3 ml_engine/feature_extractor.py")

# Optimizer
elif choice == "4":
    os.system("python3 analyzer/optimizer.py")

# ML Predictor
elif choice == "5":
    os.system("python3 ml_engine/ml_predictor.py")

else:
    print("Invalid choice")