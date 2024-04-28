num = [0] * 11
for i in range(11):
    if i <= 1:
        num[i] = 1
    elif i == 2:
        num[i] = 2
    elif i == 3:
        num[i] = 4
    else:
        num[i] = num[i-1] + num[i-2] + num[i-3]
size = int(input())
for i in range(size):
    problem = int(input())
    print(num[problem])