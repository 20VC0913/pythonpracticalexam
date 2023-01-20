def frequency(x,y):
    index=[]
    count=0
    for i in range(len(y)):
        if y[i]==x:
            count+=1
            index.append(i)
    if count==0:
        print("element",x,"is not in the list")
    else:
        print("the element",x,"has a frequency",count,"and is at indexes",index)
abc=list(input("enter the elements of the list"))
print(abc)
element=input("please enter the element to be searched")
frequency(element,abc)