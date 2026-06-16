import math
# Assuming LOG is the maximum power of 2 needed (e.g., 20 for N = 10^5, LOG = log2(N))
# up[node][i] and depth[node] are already precomputed
n = 10 
LOG = math.log2(n)
def get_lca(u, v, depth, up):
    # Step 1: Ensure u is the deeper node
    if depth[u] < depth[v]:
        u, v = v, u
        
    diff = depth[u] - depth[v]
    
    # Jump u up by 'diff' steps
    for i in range(LOG - 1, -1, -1):
        if (diff >> i) & 1:
            u = up[u][i]
            
    # If they are the same node, we found the LCA
    if u == v:
        return u
        
    # Step 2: Jump both nodes simultaneously
    for i in range(LOG - 1, -1, -1):
        if up[u][i] != up[v][i]:
            u = up[u][i]
            v = up[v][i]
            
    # The LCA is the direct parent of the current nodes
    return up[u][0]