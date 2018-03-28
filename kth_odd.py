n=raw_input()
l=len(n)
k=raw_input()
count=1
for i in range(0,l):
    if(n[i]%2!=0):
        if(count==k):
            print n[i]
