def counter(v,str):
    x=list(str)
    count=0
    for i in range(len(x)):
        if x[i] in v:
            count+=1
    if count==0:
        print("there are no vowels")
    else:
        print("no of vowels in string",count)

string=input("enter string")
print(string)
vowels=["a","e","i","o","u"]
counter(vowels,string)