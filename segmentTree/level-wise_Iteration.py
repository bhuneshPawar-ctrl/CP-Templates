class XeniaSegmentTree:
    # this template is for a problem : Xenia and Bit Operations on codeForces 
    def __init__(self, data):
        self.n = len(data)
        # 0-indexed data mapped to 1-indexed tree
        self.tree = [0] * (2 * self.n)
        
        # 1. Insert leaf nodes
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
            
        # 2. Build the tree level-by-level
        op = 1  # 1 represents OR, 0 represents XOR
        step = self.n
        
        while step > 1:
            half = step // 2
            # Process exactly one horizontal level of the tree
            for i in range(half, step):
                left_child = 2 * i
                right_child = 2 * i + 1
                
                if op == 1:
                    self.tree[i] = self.tree[left_child] | self.tree[right_child]
                else:
                    self.tree[i] = self.tree[left_child] ^ self.tree[right_child]
            
            # Arithmetic toggle: turns 1 into 0, and 0 into 1 for the next level 
            op ^= 1 
            step = half

    def update(self, pos, value):
        """
        Updates the value at data[pos] to 'value' in O(log N) time.
        """
        pos += self.n
        self.tree[pos] = value
        
        op = 1  # The first operation immediately above the leaves is always OR
        
        # 3. Move up the tree and update parents
        while pos > 1:
            pos //= 2
            left_child = 2 * pos
            right_child = 2 * pos + 1
            
            if op == 1:
                self.tree[pos] = self.tree[left_child] | self.tree[right_child]
            else:
                self.tree[pos] = self.tree[left_child] ^ self.tree[right_child]
            
            # Arithmetic toggle for the next level up
            op ^= 1 
    def query(self, idx):
        '''
        there is a critical mathematical rule you must memorize for Level-Aware
        trees: You cannot do arbitrary [L, R] range queries on an alternating tree. In a normal Sum/Max
        tree, $A + B + C$ is the same regardless of how you group them. In an alternating tree, evaluating 
        an arbitrary slice of the array breaks the strict level-by-level evaluation order. Therefore, Level-Aware
        trees almost exclusively ask for the value of the Root (index 1), or a specific fixed node
        Additionally, a Level-Aware tree must be a perfect binary tree.
         If your array length is not a power of $2$,
         , the leaves will sit at different depths, completely destroying the alternating logic.
        '''