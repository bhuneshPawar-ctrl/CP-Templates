class Trie: 
    class Node:
        def __init__(self):
            self.links = [None]*10
            self.is_end = False 

    def __init__(self):
        self.root = self.Node()

    def insert(self, num):
        num = str(num)
        ptr = self.root
        for d in num:
            idx = int(d)
            if not ptr.links[idx]:
                ptr.links[idx] = self.Node()
            ptr = ptr.links[idx]
        ptr.is_end = True 
    
    def startsWith(self, prefix):
        ptr = self.root 
        for d in str(prefix):
            idx = int(d)
            if ptr.links[idx] is None:
                return False 
            ptr = ptr.links[idx]
        return True 

    def get_common(self, num):
        ptr = self.root 
        cnt = 0 
        for d in str(num):
            idx = int(d)
            if not ptr.links[idx]: return cnt 
            cnt += 1 
            ptr = ptr.links[idx]
        return cnt 
        
    def search(self, num):
        ptr = self.root 
        for d in str(num):
            idx = int(d)
            if not ptr.links[idx]:
                return False 
            ptr = ptr.links[idx] 
        return ptr.is_end 