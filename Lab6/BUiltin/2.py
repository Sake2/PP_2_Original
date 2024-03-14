def count_up_down_letter(text):
    l =sum(1 for  i in  text if i.islower() )
    u = sum(1 for  i in  text if i.isupper() )
    return l,u
text = input()
l,u = count_up_down_letter(text)
print ("Lower case : ", l)
print("Upper Case : " , u)