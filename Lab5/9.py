import re
def containlow(text):
    text = re.sub(r'([A-Z][a-z]*)', lambda match: ' ' +match.group(1).title() , text)
    print (text)
text = input()
containlow(text)