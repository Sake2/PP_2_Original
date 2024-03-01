import re
def matchp(text):
    pattern = re.compile(r'ab{2,3}')
    if re.search(pattern,text):
        return True
    return False

text = input()
print(matchp(text))