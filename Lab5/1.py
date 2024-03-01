import re

def match_pattern(text):
    pattern = re.compile(r'^ab*$')
    if re.match(pattern, text):
        return True
    else:
        return False

print(match_pattern("abbbbb"))   # True
print(match_pattern("abb"))  # True
print(match_pattern("accc"))    # True
print(match_pattern("aab"))    # False
print(match_pattern("baaaa"))   # False
