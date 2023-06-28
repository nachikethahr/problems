n=list((input("enter the number")))
x=len(n)
a=[]
for i in range(10):
    a.insert(i,0)
for i in n:
    a[int(i)-1]+=1
print("frequency of a digits in a number:")
for i in range(10):
    print("number",i,"=",a[i])        

