import re
def containlow(text):
    listt=[]
    pattern = re.compile(r'[A-Z][^A-Z]*')
    matches = pattern.finditer(text)
    for match in matches:
        print(match.group(0));
        listt.append(match.group(0))
    return listt
text = input()
containlow(text)