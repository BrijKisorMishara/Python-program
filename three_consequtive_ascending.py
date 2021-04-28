def checklist(lst):
    for x,y,z in zip(lst,lst[1:],lst[2:]):
        if(x<y and y<z):
            return True
            break
    return False    
n=int(input("enter number of element : "))
lst=[]
for i in range(n):
    n1=int(input("enter a list : "))
    lst.append(n1)
res=checklist(lst) 
print(res)   
