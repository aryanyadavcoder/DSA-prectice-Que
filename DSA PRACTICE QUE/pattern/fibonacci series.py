def fibCalculate(fibno,fib):
	n=len(fib)
	print(fibno,n)
	for i in range(n,fibno+1):
		fib+=[fib[i-2] + fib[i-1]]
	return fib
	
	
fib=[0,1]
print(fib)
while True:
	print("0-Exit, 1- Find")
	option=int(input("Enter option \n"))
	#print(f"You entered {option}")
	if option==0:
		break
	elif option==1:
		n=len(fib)
		fno=int(input("Enter fib no\n"))
		#print("Search",fno)
		if fno<=n:
			print(f"Found fib({fno}) = {fib[fno-1]}")
			continue
		#print("Calculate")
		fib=fibCalculate(fno,fib)

		print(f"Fib:{fib}   Calculated fib({fno}) = {fib[fno-1]}")
	else:
		print("Invalid")

print("Bye")