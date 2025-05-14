t = int(input(""))
for _ in range(t):
    n = int(input(""))
    ch = input("")
    if ch[0] == ">" :
        mini = 1
        maxi = 1
    else:
        mini = 2
        maxi = 2
    print(mini,end=" ")
    for i in range(len(ch)):
        if ch[i] == ">" :
            print(maxi+1, end=" ")
            maxi = maxi +1
        else:
            print(mini-1 , end=" ")
            mini = mini - 1
    print()
