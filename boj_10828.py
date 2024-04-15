import sys
input = sys.stdin.readline
trial = int(input())
stack = list()
for i in range(trial):
    order = input().split()
    if order[0] == 'push':
        stack.append(order[1])
    elif order[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif order[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'size':
        print(len(stack))
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())