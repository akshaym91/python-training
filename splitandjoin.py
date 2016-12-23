import os
import sys

text = "Thsi, is the text text that is going , to be operated upon."

split_with_spaces = text.split()
print(split_with_spaces)
joined_after_spacing = ' '.join(split_with_spaces)
print(joined_after_spacing)
split_with_comma = text.split(',')
print(split_with_comma)
joined_with_comma = ','.join(split_with_comma)
print(joined_with_comma)
