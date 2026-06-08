results = [0, 1]   
ninputs = 5
i = 1

while i <= ninputs:
    n = int(input("Enter number: "))
    if n < len(results):
        print(n, results[n])
        i += 1
        continue
    for j in range(len(results), n + 1):
        results.append(results[j-1] + results[j-2])
    print(n, results[n])
    i += 1

print("All Fibonacci:", results)