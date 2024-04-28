num = [0 for i in range(1001)]
limit = int(input())
for i in range(limit+1):
    if i == 0:
        num[i] = 1
    elif i == 1:
        num[i] = 1
    else:
        num[i] = (num[i-1] + num[i-2]) % 10007
print(num[limit])