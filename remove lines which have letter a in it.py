file=open("string.txt")
lines=file.readlines()
file.close()
file=open("string.txt","w")
file1=open("string1.txt","w")
for line in lines:
    if "a" in line:
        file.write(line)
    else:
        file1.write(line)
file.close()
file1.close()