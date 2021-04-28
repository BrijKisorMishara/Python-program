def evenodd(l):
    even=[]
    odd=[]
    for j in l:
        if j%2==0:
            even.append(j)
        else:
            odd.append(j)
    return even,odd        
num=[]
n=int(input("enter number of element : "))
for i in range(n):
    n1=int(input("enter element : \t"))
    num.append(n1) 
n1,n2=evenodd(num)  
print("list : {}\t even : {}\t odd {}".format(num,n1,n2))
