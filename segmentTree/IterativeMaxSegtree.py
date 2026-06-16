class MaxSegmentTree:
    def __init__(self, data):
        self.n = len(data)
        # 0-indexed data mapped to 1-indexed tree for easy bitwise math
        self.tree = [float('-inf')] * (2 * self.n)
        
        # Insert leaf nodes
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
            
        # Build the tree by calculating parents
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, pos, value):
        """
        Updates the value at data[pos] to 'value' in O(log N) time.
        """
        pos += self.n
        self.tree[pos] = value
        
        # Move up the tree and update parents
        while pos > 1:
            pos //= 2
            self.tree[pos] = max(self.tree[2 * pos], self.tree[2 * pos + 1])

    def query(self, left, right):
        """
        Returns the maximum in the inclusive range [left, right] in O(log N) time.
        """
        # Convert to leaf node indices
        left += self.n
        right += self.n
        
        res = float('-inf')
        
        while left <= right:
            # If left is a right child, process it and move to the right
            if left % 2 == 1:
                res = max(res, self.tree[left])
                left += 1
                
            # If right is a left child, process it and move to the left
            if right % 2 == 0:
                res = max(res, self.tree[right])
                right -= 1
                
            # Move to parents
            left //= 2
            right //= 2
            
        return res
# both min and max seg_Tree
class SegTree:
    def __init__(self, data):
        self.n = len(data)
        inf = float('inf')
        neg_inf = float('-inf')
        self.min_tree = [inf]*(2*self.n) 
        self.max_tree = [neg_inf]*(2*self.n)
        for i in range(self.n):
            self.min_tree[i + self.n] = data[i]
            self.max_tree[i + self.n] = data[i]
        for i in range(self.n - 1, -1, -1):
            self.min_tree[i] = min(self.min_tree[2*i], self.min_tree[2*i + 1])
            self.max_tree[i] = max(self.max_tree[2*i], self.max_tree[2*i + 1])
    
    def query(self, l, r, type):
        l += self.n
        r += self.n
        res = float('inf') if type == 0 else float('-inf')
        while l <= r: 
            if l % 2 != 0: 
                if type == 0: 
                    res = min(res, self.min_tree[l])
                else:
                    res = max(res, self.max_tree[l])
                l += 1
            if r % 2 == 0: 
                if type == 0: 
                    res = min(res, self.min_tree[r])
                else:
                    res = max(res, self.max_tree[r])
                r -= 1
            l //= 2
            r //= 2 
        return res  
# --- Template Usage ---
# arr = [1, 5, 2, 4, 3]
# seg_tree = MaxSegmentTree(arr)
# print(seg_tree.query(0, 3))  # Max in arr[0...3] -> 5
# seg_tree.update(2, 10)       # arr becomes [1, 5, 10, 4, 3]
# print(seg_tree.query(0, 3))  # Max in arr[0...3] -> 10
