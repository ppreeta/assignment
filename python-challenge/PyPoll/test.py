x = [1,1,2,2,3,4,5]
b=[]
#b=set(x)
for i in x:
    if i not in b:
        b.append(i)
print(b)
