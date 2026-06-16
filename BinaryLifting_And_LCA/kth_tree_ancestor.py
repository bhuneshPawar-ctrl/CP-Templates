import math
class TreeAncestor:
    def __init__(self, n: int, parent):
        self.n = n 
        cols = int(math.log2(n) + 1)
        ancestor = [[-1]*cols for _ in range(n)]
        for i in range(n): 
            ancestor[i][0] = parent[i]
        for j in range(1, cols): 
            for node in range(1, n):
                if ancestor[node][j - 1] != -1:
                    ancestor[node][j] = ancestor[ancestor[node][j - 1]][j - 1]
        self.ancestor = ancestor

    def getKthAncestor(self, node: int, k: int) -> int:
        curr = node 
        for i in range(k.bit_length() - 1, -1, -1):
            if curr == -1: break 
            if k & (1 << i) != 0: 
                curr = self.ancestor[curr][i]
        return curr 