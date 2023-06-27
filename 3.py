s = list(map(str, input().split()))
s.sort(reverse=True)
print(int(''.join(s)))