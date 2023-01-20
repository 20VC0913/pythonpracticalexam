import pickle
sdata={}
slist=[]
file=open("student.dat","wb")
number=int(input("how many number of students?:"))
for i in range(number):
    name=input("enter the name of the student")
    rollnumber=int(input("enter the roll number of the student"))
    sdata[rollnumber]=name
    slist.append(sdata)
    sdata={}
pickle.dump(slist,file)
file.close()
x=open("student.dat","rb")
sdata=pickle.load(x)
print(sdata)
rollnumber=int(input("enter the roll number you want to search for:"))
for line in sdata:
    if rollnumber in line:
        print(line)
        count+=1
    else:
        count=0
if count==0:
    print("not found")