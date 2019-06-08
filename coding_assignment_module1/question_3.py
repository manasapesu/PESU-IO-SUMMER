inp=list(map(int,input("Enter the list of numbers seperated by comma: ").split(",")))
inp.sort()
num=int(input("Enter number to search: "))
high=len(inp)-1
low=0
print("The sorted list:",inp)

while 1:
    mid=(high+low)//2
    if num==inp[mid]:
        print("The number is at",mid)
        break
    elif low==high:
        print("The given number is not in the list")
        break
    elif num<inp[mid]:
        high=mid-1
    elif num>inp[mid]:
        low=mid+1
    
        
