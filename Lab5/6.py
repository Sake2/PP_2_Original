import re
def containlow(text):
    text = re.sub('[.| |,]',':',text)
    print(text)
text = input()
containlow(text)