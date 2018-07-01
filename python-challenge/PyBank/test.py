a=[1,2,8,9]
x=[]
for i in range(1,len(a)):
    x.append(a[i] - a[i-1])
print(x)
