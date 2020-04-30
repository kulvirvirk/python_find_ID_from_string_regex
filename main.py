
# 1. provide a string with ID: with format A999111

import re


string_with_id = ('Hello, my id is A123456')

# create regex for to capture: 
# - alphabets A to Z and lowercase a to z = [[A-Za-z]]
# - digits 0 to 9 for next 6 positons = \d\d\d\d\d\d
# - combine both with raw string = r'[A-Za-z]\d\d\d\d\d\d'
id_regex = re.findall(r'[A-Za-z]\d\d\d\d\d\d', string_with_id)
print(id_regex)