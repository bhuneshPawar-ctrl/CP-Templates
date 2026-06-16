'''
Because you are now using C-level reading, you need to remember exactly one rule about sys.stdin.readline: It does not remove the invisible newline character (\n) at the end of a line.

For Integers/Arrays: You are 100% safe. Python's int() and .split() automatically ignore invisible newline characters. Your current x = int(input()) and arr = list(map(int, input().split())) will work flawlessly.

For Strings: If an OA problem gives you a raw string (like "abacaba"), calling s = input() will store it as "abacaba\n". This will ruin any string length checks or character comparisons.

The Fix: Whenever an OA requires you to read a single string, just add .strip() to chop off the hidden newline:
'''
# for string input(): s = input().strip()
import math,heapq
from collections import defaultdict,deque
import sys
input = sys.stdin.readline
def helper():
    return 
def main():
    def solve(a):
        return 
    n = int(input())
    arr = list(map(int, input().split()))
    
    a = 0
    b = solve(a)
    ans = 0
    return ans 

t = int(input())
for _ in range(t):
    print(main())