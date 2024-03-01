import re
def containlow(text):
    text = re.sub(r'([^A-Z])([A-Z][a-z]*)', lambda match: '_' + match.group(2).title() , text)
    print (text)
text = input()
containlow(text)