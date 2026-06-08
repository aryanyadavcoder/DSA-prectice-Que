a = "I am reading python!"
result = ""
for i in a:
    if i.isalnum() or i.isspace():
        result+=i
print(result)        