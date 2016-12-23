# Experiments day 2
# 1. Import the module in the same folder
# 2. Import the module in a different folder.
# 3. Exercise: Work with .xls file.
# 4. Usage of comma operator
# 4. Importing your own module in the same folder
# 5. Import your module in a different module.
# 6. Download xlrd and work with it.
# 7. Function which does not take any argument  and does not return anything.
# 8. Function which returns value
# 9. Function which takes argument a. passing value
#                                  b. passing variables
# 10. Passing values with name (2 use cases)
# 11. Parameters with default values and mandatory values
# 12. Default arguments from right hand side and otherwise
# 13. Recursion a. treshold
#               b. factorial
# 14. LEGB: usage of global keyword
# 15. Nesting of functions
# 16. Pass by object (mutable and immutable)
# 17. Positional and keyword arguments
# 18. docstring, import, dir, type and help.
# -----------------------------------------------------------------------
# 19. cat dummy.text with python fileoperations.py fileoperations.txt
# 20. cp a.txt b.txt with python fileoperations.py a.txt b.txt
# 21. wc c.txt
# 22. Write and read back with and without seek.
# 23. Split and Join using ',' and ' ' as the delimiter.
# -----------------------------------------------------------------------
# Exercise 2:
# Create a  Menu driven a. simple calculator: add, subtract, multiply, divide, goback
#                       b. scientic calculator: sine, cosine, sqrt, power, goback
#                       c. exit
#  calc_menu.py and calc_operations.py
#

import xlrd

file = xlrd.open_workbook(filename="PerformanceAnalysis.xlsx")
sheet = file.sheet_by_index(0)
cell00 = sheet.cell_value(0, 0)
print(cell00)
