n=int(input())
def summation(n):
    
    lst1=[]
    lst2=[]
    for i in range(n):
        x=int(input())
        lst1.append(x)
        
    for i in range(n):
        x=int(input())
        
        lst2.append(x)
    total=0
    updated_list=[]
    for i in range(n):
        total=lst1[i]+lst2[i]
        updated_list.append(total)
    return updated_list 
def find_min_max(updated_list):
    x=min(updated_list)
    y=max(updated_list)
    return x,y
updated_list=summation(n)
print(updated_list)
print(find_min_max(updated_list))# YOUR CODE HERE
