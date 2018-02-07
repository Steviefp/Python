lines=[]
f=open('test.txt','r')
for x in f:
    lines.append(x.strip())
print(lines)