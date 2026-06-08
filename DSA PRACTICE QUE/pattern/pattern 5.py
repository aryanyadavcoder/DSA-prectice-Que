n = 7
for row in range(1,n+1):
    for col in range(1,n+1):
        condition = row+col==n+1 and row>4  or row==col and row>=4 or row == 6 and col == 4
        if condition:
            print("*",end="")
        else:
            print(" ",end="")
    print()            
    
print()    
n = 7
mid = (n+1)//2
for row in range(1, n+1):
    for col in range(1, n+1):
        condition = col==1 or row==1 and col<=mid or col==4 and row<=mid or row==mid and col<=mid or row-col==mid-1
        if condition:
            print('*',end=" ")
        else:
            print(" ", end=" ")
    print()   
print() 


n = 7
mid = (n+1)//2
for row in range(1, n+1):
    for col in range(1, n+1):
        condition = row+col==n+1 or row==col and col<=mid
        if condition:
            print('*',end=" ")
        else:
            print(" ", end=" ")
    print() 
print()

n = 7
for row in range(1,n+1):
    for col in range(1,n+1):
        condition = row+col==n+1 and row>4  or row==col and row>=4 or row == 6 and col == 4
        if condition:
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()

n = 7
for row in range(1,n+1):
    for col in range(1,n+1):
        condition = (row>=1 and row<=7 and col==1) or (row==col)  or (row>=1 and row<=7 and col==n)
        if condition:
            print("*",end="")
        else:
            print(" ",end="")
    print()             