a=[]
n=int(input("enter the number of elements to be enter:"))
print("ente the numebrs")
ele=0
c=0
while c<n:
    ele=input()
    a.append(ele)
    c+=1
sum=0
for i in a:
    sum+=int(i)
mean=float(sum)/n
sum=0
for i in a:
    diff=0
    diff=mean-int(i)
    if diff>0:
        sum+=diff**2
    else:
        b=abs(diff)
        #the abs() function works as mathematical mod
        sum+=b**2
var=sum/(n-1)
sd=var**0.5 #here you can use sqrt() function also
print("mean value:",mean) 
print("standard deviation:",sd)
print("variance:",var)       
                           