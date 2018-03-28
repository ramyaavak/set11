n=raw_input()
l=len(a)
k=raw_input()
count=0
for i in range(0,l):
    if(n[i]==k):
      count=count+1
if(count>0):
   print "yes"
else:
   print "no"
       
