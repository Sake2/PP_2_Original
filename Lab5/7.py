import re
def snake_to_camel(snake_str):
    camel_str = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), snake_str)
    print(camel_str)

text = input()
snake_to_camel(text)