# Creating Function :: 

def Binary_Search(li,n,start,end) :
    
    # base case :
    if start==end :
        
        if li[start]==n :
            return start
        
        else :
            return -1
    else :
        
        mid = int((start+end)/2)
        if li[mid] == n :
            return mid
        
        elif li[mid]>n :
            # left half :
            return Binary_Search(li,n,start,mid-1)
        
        else :
            # right half :
            return Binary_Search(li,n,mid+1,end)
        
# Taking The List Dynamicaly & Sorting The List.  //  Though Binary Search Always Acceept sorted List . Here We Sorting It Dynamicly... ::
            
v = input("Enter The Numbers Seperated by Comma(,) : ").split(',')      
li = []
for i in v :
    
    i = int(i)
    li.append(i)
li = sorted(li)
print("Your list Is Sorted Now : ",li)

# Calling The Function & Printing It's Position ::

n = int(input("Enter The Search Element : "))
index = Binary_Search(li,n,0,len(li)-1)
if index == -1 :
    print("Element Not Found !")
    
else :
    print(n," Is Found At Position",index+1)

        
