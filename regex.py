# Glob is wildcard or meta characters and is different from regexp. Ex: ls *.py
# Glob is applied  at the names of files and folders.
# Regexp is used for the contents of the files.
# Grep is combination of glob and regexp.
# 1. Print the all the python files in the folder.
import glob
import re

print glob.glob('*.py')

# Find out number of occurances of abc
str1 = "This it the different types pattern matchning. One is called."
print len(re.findall(pattern, str1))

# Glob:
# * - Any character any number of times.
# ? - One character
# ls ???.py
# ls *.py
#
# Regular Expression:
# . - any character one occurance
# ? - 0 or 1 occurance of previous regular expression Ex: a?b -------------- b ab
# * - 0 or more occurance of previous regular expression Ex: ab*cd --------- acd abcd abbcd abbbcd
# + - 1 or more occurance of previous regular expression Ex: ab*cd --------- abcd abbcd abbbcd
# [] - range expression Ex: ab*cd ---- abcd abbcd abbbcd Ex:
#                                                            i[aA]j -------- iaj iAj
#                                                            i[a]j --------- iaj
#                                                            i[a-z]j ------- iaj - izj
#                                                            i[a-zA-Z]j ---- iaj - iZj
#                                                            i[a-zA-Z0-9]j - iaj - i9j
# [^] - Negated range. Caret has to be at the beginning. Ex:
#                                                            i[^aA]j -------- not (iaj iAj)
#                                                            i[^a]j --------- not(iaj)
#                                                            i[^a-z]j ------- not(iaj - izj)
#                                                            i[^a-zA-Z]j ---- not(iaj - iZj)
#                                                            i[^a-zA-Z0-9]j - not(iaj - i9j)
# {,} - Minimum and Maximum Ex:
#                                                            a{1,2}b -------- ab aab
#                                                            i{,2}j --------- j ij iij
#                                                            i{2}j ---------- iij iiij ...
# () - Grouping                                        Ex: (ca)?b -------------- b cab
# Anchor elements:
# ^ - at the beginning ^Avaya
# $ - at the beginning Avaya$
# Miscellaneous elements:
# \s - White Space
# \d - digit
# \S - Non White Space
# \D - Nondigit
#
# 1. Create a pattern to match for a.b :
#   a[.]b
#   a\.b
#   (a.)b
#
# Create a pattern to match for IP Address.
#([0-9]{1,2}[0-5].){3,3}[0-9]{1,2}[0-5]
