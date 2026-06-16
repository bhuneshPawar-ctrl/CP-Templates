class segTree:
    def merge(self, idx):
        self.tree[idx] = self.tree[2*idx + 1] + self.tree[2*idx + 2]
        return 
    
    def __init__(self, data):
        def buildTree(l, r, idx):
            if l == r: 
                tree[idx] = data[l]
                return 
            mid = l + (r - l) // 2
            buildTree(l, mid, 2*idx + 1)
            buildTree(mid + 1, r, 2*idx + 2)
            self.merge(idx)
            return
        self.data = data 
        self.n = len(data)
        self.lazy = [0]*(4*self.n)
        tree = [0]*(4*self.n)
        buildTree(0, self.n - 1, 0)
        self.tree = tree 

    def updateTree(self, l, r, idx, update_idx):
        if l == r: 
            self.tree[idx] = 0
            return 
        mid = l + (r - l) // 2
        if update_idx <= mid: 
            self.updateTree(l, mid, 2*idx + 1, update_idx)
        else:
            self.updateTree(mid + 1, r, 2*idx + 2, update_idx)
        self.merge(idx)
        return
    
    def push_down_lazy(self, idx, l, r):
        self.tree[idx] += self.lazy[idx]*(r - l + 1)
        if l != r and self.lazy[idx] != 0: 
            self.lazy[2*idx + 1] += self.lazy[idx]
            self.lazy[2*idx + 2] += self.lazy[idx]
            self.lazy[idx] = 0 

    def updateTree_range(self, start, end, idx, l, r, val):
        self.push_down_lazy(idx, l, r)
        if l > end or r < start: return 
        if l >= start and r <= end: 
            self.tree[idx] += (r - l + 1)*val 
            if l != r: 
                self.lazy[2*idx + 1] += val
                self.lazy[2*idx + 2] += val
            return 
        mid = l + (r - l) // 2
        self.updateTree_range(start, end, 2*idx + 1, l, mid, val)
        self.updateTree_range(start, end, 2*idx + 2, mid + 1, r, val)
        self.merge(idx)

    def queryTree_lazy(self, start, end, idx, l, r):
        self.push_down_lazy(idx, l, r) 
        if l > end or r < start: return 0 
        if l >= start and r <= end:
            return self.tree[idx]
        mid = l + (r - l) // 2
        left = self.queryTree_lazy(start, end, 2*idx + 1, l, mid)
        right = self.queryTree_lazy(start, end, 2*idx + 2, mid + 1, r)
        return left + right 
    
    # def queryTree(self, val, idx, l, r):
    #     if l == r: 
    #         if self.tree[idx] < val: return -1
    #         return l
    #     mid = l + (r - l) // 2 
    #     left = self.tree[2*idx + 1]
    #     right = self.tree[2*idx + 2]
    #     if max(left, right) < val: return -1 
    #     if left >= val: 
    #         return self.queryTree(val, 2*idx + 1, l, mid)
    #     return self.queryTree(val, 2*idx + 2, mid + 1, r)