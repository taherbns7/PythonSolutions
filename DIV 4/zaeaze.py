t = int(input())
for _ in range(t):
    n = int(input())
    ch = input()
    l = []
    for i in range(n - 1):
        l.append(ch[i] + ch[i + 1])
    found = False
    seen = {}
    for i in range(len(l)):
        if l[i] in seen:
            if seen[l[i]] == i - 1:
                continue  
            found = True
            break
        seen[l[i]] = i
    print("YES" if found else "NO")
