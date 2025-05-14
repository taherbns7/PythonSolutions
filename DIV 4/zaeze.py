def optimized_sieve(limit):
    if limit < 2:
        return []

    sieve = [True] * ((limit // 2) + 1)
    sieve[0] = False  # 1 is not prime

    for i in range(1, int(limit**0.5) // 2 + 1):
        if sieve[i]:
            step = 2 * i + 1
            for j in range(2*i*(i + 1), len(sieve), step):
                sieve[j] = False

    primes = [2] + [2*i + 1 for i, is_p in enumerate(sieve) if is_p]
    return primes
def squared_primes_set(limit):
    primes = optimized_sieve(limit)
    return {p ** 2 for p in primes}
x = int(input())
L = list(map(int,input().split()))

S = squared_primes_set(1000000)
for x in L :
    if x in S :
        print("YES")
    else:
        print("NO")
    
