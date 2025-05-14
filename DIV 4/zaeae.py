def get_priority(L):
    
    return sum(L) / len(L)

def trim_and_recompute(L):
    
    if len(L) > 1:
        L.pop()  
    return get_priority(L)  

t = int(input())  
for _ in range(t):
    n, m = map(int, input().split())  
    L = []
    
    for i in range(n):
        L.append(list(map(int, input().split())))  

    priority = []
    if n == 1:
        # Directly calculate the cumulative sum for the single list
        bigL = L[0]
        cumulative_sum = 0
        total_sum = 0
        for num in bigL:
            cumulative_sum += num
            total_sum += cumulative_sum
        print (total_sum)
        break
        
    for i in range(n):
        current_list = L[i]
        avg = get_priority(current_list)
        priority.append([avg, i, current_list.copy()])  
    while True:
        priority.sort(reverse=True, key=lambda x: (x[0], len(x[2])))

        avg1, idx1, list1 = priority[0]
        avg2, idx2, list2 = priority[1]

        if avg1 == avg2:
            avg1 = trim_and_recompute(list1)
            avg2 = trim_and_recompute(list2)

            priority[0][0] = avg1
            priority[1][0] = avg2
        else:
            break
    
    bigL = []
    for avg, idx, _ in priority:
        bigL.extend(L[idx])  
    cumulative_sum = 0
    total_sum = 0

    for num in bigL:
        cumulative_sum += num
        total_sum += cumulative_sum

    print(total_sum)
