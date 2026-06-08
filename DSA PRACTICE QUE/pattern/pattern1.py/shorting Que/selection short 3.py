a = [1, 4, 7, 6, -3]
n = len(a)
print(f"Start: {a}")
for i in range(n-1):
    minpos = i
    for j in range(i+1, n):
        print(
            f"Comparing pos {j}<{minpos}, values {a[j]}<{a[minpos]} , {a[j] < a[minpos]}")

        if a[j] < a[minpos]:
            minpos = j
    a[i], a[minpos] = a[minpos], a[i]
    print(f"After {i+1} loop: {a}")
print(f"Final: {a}")
