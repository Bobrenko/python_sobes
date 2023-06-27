import re

s = input()
result = re.findall('\d+', s)
for i in range(len(result)):
    if i / 2 != 1 and i != 0:
        result[i] = '00' + result[i]
    else:
        if int(result[i]) // 1000 == 0:
            result[i] = '0' + result[i]
for i in range(0, len(result), 2):
    result[i] = result[i] + "/" + result[i+1]
del result[1:len(result):2]
print(*result, sep='\n')
