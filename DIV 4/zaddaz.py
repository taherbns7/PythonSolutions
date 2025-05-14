s = input("")
check1 = False
check2 = False
l=[]
for i in range(len(s)-1):
  if i in l :
    continue
  if(check1== False):
    if s[i] == "A":
      if s[i+1]=="B" :
        check1 = True
        l.append(i+1)
  elif(check2 == False and check1==True):
    if s[i] == "B":
      if s[i+1]=="A" :
        check2 = True
        l.append(i+1)
if (check1) and (check2):
  print("YES")
else:
  check1 = False
  check2 = False
  l=[]
  for i in range(len(s)-1):
    if i in l :
      continue
    if(check1== False):
      if s[i] == "B":
        if s[i+1]=="A" :
          check1 = True
          l.append(i+1)
    elif(check2 == False and check1==True):
      if s[i] == "A":
        if s[i+1]=="B" :
          check2 = True
          l.append(i+1)
  print(check1,check2)
  print(l)
  if (check1) and (check2):
    print("Yes")
  else:
    print("NO")
  
