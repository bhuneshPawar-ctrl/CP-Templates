def get_spf(n: int):
    spf = list(range(n + 1))
    for i in range(2, int(n**0.5) + 1):
        if spf[i] == i:  # i is prime
            for j in range(i * i, n + 1, i):
                if spf[j] == j:  # Mark only if not previously marked by a smaller prime
                    spf[j] = i
                    
    return spf

def get_prime_factors(x: int, spf: list[int]):
    factors = []
    while x != 1:
        factors.append(spf[x])
        x //= spf[x]
    return factors