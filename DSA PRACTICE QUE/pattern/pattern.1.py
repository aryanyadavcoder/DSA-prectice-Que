n = 7
for row in range(1,n+1):
    for col in range(1,n+1):
        condition = row-col==3 or  col == 2 and row==3 or row+col == 11 or col==6 and row==3 or row==4 and col==4
        if condition: 
            print(0,end="")
        else:
            print(" ",end="")
    print()                