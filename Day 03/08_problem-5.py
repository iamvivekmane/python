# comment spam or not spam
comment = input("Enter comment : ")
flag = False
comment.lower()
if "make a lot of money" in comment:
    flag = True
elif "buy now" in comment:
    flag = True
elif "subscribe this" in comment:
    flag= True
elif "click this" in comment:
    flag = True

if(flag):
    print("spam")
else:
    print("not spam")