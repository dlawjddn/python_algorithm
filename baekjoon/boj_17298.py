size = int(input())
number = list(map(int, input().split()))
stack = list()
ans = [-1] * size
for i in range(size):
    while stack and number[stack[-1]] < number[i]:
        ans[stack.pop()] = number[i]
    stack.append(i)
print(*ans)