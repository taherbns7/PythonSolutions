t = int(input())
for _ in range(t):
    p = input()
    s = input()
    if p == s:
        print("YES")
    elif len(p) == len(s) and p != s:
        print("NO")
    else:
        i = 0
        j = 0
        ok = True
        while i < len(p) and j < len(s):
            if p[i] != s[j]:
                ok = False
                break
            count_p = 1
            while i + 1 < len(p) and p[i] == p[i + 1]:
                i += 1
                count_p += 1
            count_s = 1
            while j + 1 < len(s) and s[j] == s[j + 1]:
                j += 1
                count_s += 1
            if count_s < count_p or count_s > 2 * count_p:
                ok = False
                break
            i += 1
            j += 1
        if i != len(p) or j != len(s):
            ok = False
        print("YES" if ok else "NO")
                
    
