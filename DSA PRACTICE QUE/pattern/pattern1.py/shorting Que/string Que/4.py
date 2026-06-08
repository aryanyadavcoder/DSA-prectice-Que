# text = "programming"
def isLetter(ch):
	ch=ord(ch)
	if ch>=ord('A') and ch<=ord('Z'):
		return True
	if ch>=ord('a') and ch<=ord('z'):
		return True
	return False
s="Count total words in a sentence".strip()
s=f" {s} "
count=0
#print(s)
n=len(s)
for i in range(1,n):
	prev,next=s[i-1],s[i]
	#print(prev,next)
	if isLetter(prev) and not isLetter(next):
		count+=1
print(f"{s} has {count} words.")