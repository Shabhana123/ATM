x=int(input("enter how much amount you want to withdraw:"))
y=int(input("enter total amount in your bank:"))
z=float(input("enter transaction charges:"))
if (x%5==0):
    print("after your transaction you have :",y-x-z)
elif(x%5!=0):
    print("incredentials:",y)
elif(x>y):
    print("can't do transaction:",y)
else:
    print("good bye")
    
