def changer(y):
    changed=[]
    for i in range(len(y)):
        if int(y[i])%2==0:
            changed.append(int(int(y[i])/2))
        else:
            changed.append(int(2*int(y[i])))
    print(changed)
y=list(input("enter the list:"))
changer(y)