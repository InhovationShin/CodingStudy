import sys
input = sys.stdin.readline
n, k = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))
s.sort(key=lambda x : (-x[1], -x[2], -x[3]))
for i in range(n):
    if s[i][0] == k:
        idx = i
for i in range(n):
    if s[idx][1:] == s[i][1:]:
        print(i + 1)
        break