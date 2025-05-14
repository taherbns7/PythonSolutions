t = int(input(""))
for _ in range(t):
    s0,s1 = map(str,input("").split())
    print( s1[0] + s0[1] + s0[2] + " " + s0[0] + s1[1] + s1[2] )
