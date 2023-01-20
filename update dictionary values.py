def updater(d,k,v):
    d[k]=v
    print(d)

dict1={}
no=int(input("how many records do you want in your dictionary?"))
for i in range(no):
    key=input("enter the key:")
    value=input("enter the value:")
    dict1[key]=value
    key=None
    value=None
print(dict1)
key=input("which key do you want to update?")
value=input("enter new value for the key")
updater(dict1,key,value)