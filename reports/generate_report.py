report = """
====================================
      RTL ANALYSIS REPORT
====================================

Module Analyzed : bad_design

WARNINGS:
------------------------------------
1. Redundant self-assignment detected
2. Possible inefficient RTL coding style

RECOMMENDATIONS:
------------------------------------
- Remove unnecessary assignments
- Simplify sequential logic

STATUS:
------------------------------------
Analysis Completed Successfully
"""

file = open("output/report.txt", "w")

file.write(report)

file.close()

print("Report Generated Successfully")