import re

user_input="The subject has Age:25 and Height:180cm.Other details are not relevant.Weight:70kg was noted."

def extract_data(text):
    pattern=r'[a-zA-Z]+:[a-zA-Z0-9]+'
    return re.findall(pattern, text)

def better_extract_data(text):
    pattern=r'([a-zA-Z]+):([a-zA-Z0-9]+)'
    return re.findall(pattern, text)

print(extract_data(user_input))
print(better_extract_data(user_input))