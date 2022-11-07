import sys

T = int(input()) #Test case
for i in range(T):
        a,b = map(int, sys.stdin.readline().rstrip().split())
        print(a+b)