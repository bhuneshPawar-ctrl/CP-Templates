import sys
# import math,heapq
# from collections import defaultdict,deque
# sys.setrecursionlimit(300005)
def solve():
    pass

def main(get_int, get_str):
    n = get_int()
    arr = [get_int() for _ in range(n)]
    # s = get_str()
    return 

def start():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    data_stream = iter(input_data)
    
    def get_int():
        return int(next(data_stream))
        
    def get_str():
        return next(data_stream)
        
    # Read the number of test cases. 
    # (If the problem doesn't use test cases, delete this try-except block and the for-loop).
    try:
        t = get_int()
    except StopIteration:
        return

    out = []

    for _ in range(t):
        ans = main(get_int, get_str)
        out.append(str(ans))
        #print(ans)
    
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    start()