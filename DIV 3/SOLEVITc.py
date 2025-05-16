n = int(input(""))
for _ in range(n):
   a,k = map(int,input("").split())
   l = list(map(int,input().split()))
   r = k % a
   m=[]
   for i in range(r):
       m.append(l[a-1-i])
   for i in range(a-r):
       m.append(l[i])
   e=1
   for x in range (len(m)):
       if m[x] == x+1 and m[x]%a == r :
           print("YES")
           e = 0
           break
   if ( e != 0 ) :
       print("NO")
       
   
    
