a = [[1, 3],
     [1, 4]]

b = [[5, 1],
     [2, 6]]


def printMatrix(a):
    nrows, ncols = len(a), len(a[0])
    for row in range(nrows):
        for col in range(ncols):
            print(f"{a[row][col]:<4}", end="")
        print()
result = []
for i in range(len(a)):
    row = []
    for j in range(len(a[0])):
        row.append(a[i][j] + b[i][j])
    result.append(row)
printMatrix(result)
