from functools import reduce
n = int(input())
k = int(input())
s = []
for i in range(n):
    s.append(int(input()))
for i in range(k):
    a = reduce(max, s)
    s.remove(a)
    a /= 2
    s.append(a)
    s.append(a)
for i in range(len(s)):
    print(s[i])
