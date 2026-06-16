val = 200005
mod = 998244353

# 1. Global Precomputation
fact = [1] * (val + 1)
inv = [1] * (val + 1)

# Build forward factorials
for i in range(1, val + 1):
    fact[i] = (fact[i - 1] * i) % mod 

# Build backward inverses
# A) Calculate the heaviest inverse exactly ONCE using Fermat's
inv[val] = pow(fact[val], mod - 2, mod)

# B) Propagate the inverses backward in strict O(N) time
# 1 / fact(i)  = (1 / fact(i + 1)) * (i + 1)
for i in range(val - 1, -1, -1):
    inv[i] = (inv[i + 1] * (i + 1)) % mod

# O(1) Combination Lookup
def nCr(n, r):
    if r < 0 or r > n: return 0
    return fact[n] * inv[r] % mod * inv[n - r] % mod