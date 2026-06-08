n = 7
for row in range(1, n+1):
    for col in range(1, n+1):
        condition = (row==col) or (row+col==8) or (row==1 and col>=1 and col<=7) or (row==7 and col>=1 and col<=7)
        if condition:
            print('*',end=" ")
        else:
            print(" ", end=" ")
    print() 
print()