import re
def containlow(text):
    pattern = re.compile(r'[a-z_]+')
    matches = pattern.finditer(text)
    for match in matches:
        print(match.group(0));
text = input()
containlow(text)