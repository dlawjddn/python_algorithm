from collections import deque

string = input()
stack = list()
ans = list()
check_point = False
for i in string:
    if check_point:
        if i == '>':
            ans.append(i)
            check_point = False
        else:
            ans.append(i)
    else:
        if i == '<':
            while stack:
                ans.append(stack.pop())
            ans.append(i)
            check_point = True
        elif i == ' ':
            while stack:
                ans.append(stack.pop())
            ans.append(i)
        else:
            stack.append(i)
while stack:
    ans.append(stack.pop())

print(''.join(ans))