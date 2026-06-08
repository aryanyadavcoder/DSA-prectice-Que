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
