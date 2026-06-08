a = [1, 4, 7, 6, -3]

n = len(a)
print(f"Start: {a}")
for i in range(n-1):
    minpos = i
    for j in range(i+1, n):
        if a[j] < a[minpos]:
            minpos = j
    a[i], a[minpos] = a[minpos], a[i]
    print(f"After {i+1} loop: {a}")
print(f"Final: {a}")
