size = int(input())
numbers = list(map(int, input().split()))
count = dict()
stack = list()
ans = [-1] * size
for i in numbers:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for i in range(size):
    while stack and count[numbers[stack[-1]]] < count[numbers[i]]:
        ans[stack.pop()] = numbers[i]
    stack.append(i)
print(*ans)
