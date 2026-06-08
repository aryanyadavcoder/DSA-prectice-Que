a = [1,2,4,6,9,10]
b = [3,4,7,8,9,12,13]
n1 = len(a)
n2 = len(b)
c = [0 for r in range(n1+n2)]
i, j, k = 0, 0, 0
while i <= n1-1 and j <= n2-1:
    if a[i] <= b[j]:
        c[k] = a[i]
        i += 1
        k += 1
    else:
        c[k] = b[j]
        j += 1
        k += 1
while j < n2:
    c[k] = b[j]
    j += 1
    k += 1
print(c)