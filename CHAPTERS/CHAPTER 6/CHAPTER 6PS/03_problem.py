p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

comment = input("Enter your comment here: ")

if(comment in p1 or comment in p2 or comment in p3):
    print("Its a spam message: ")
    
else:
    print("its not a spam message")