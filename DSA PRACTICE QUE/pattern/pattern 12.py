n = 5
for row in range(n,0,-1):
    for i in range(1, n - row + 1):
        print(" ", end="")
    for j in range(1, 2*row ):
        print("0", end="")
    print()
