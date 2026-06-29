def mul_matrix(m1, m2):
    r1, c1, r2, c2 = len(m1), len(m1[0]), len(m2), len(m2[0])
    ans = [[0]*c2 for _ in range(r1)]
    for i in range(r1): 
        for j in range(c2): 
            for k in range(r2): 
                ans[i][j] = (ans[i][j] + m1[i][k]* m2[k][j]) % MOD
    return ans 

def matrixExp(mat, p, I):
    r = len(mat)
    if p == 0: 
        return  I 
    res = matrixExp(mat, p // 2, I)
    res = mul_matrix(res, res)
    if p & 1 != 0: 
        res = mul_matrix(res, mat)
    return res 
MOD = 10**9 + 7 