steel = list(input())
stack = list()
ans = 0
laser = False
for i in steel:
    if i == '(':
        laser = True
        stack.append(i)
    else:
        if laser:
            laser = False
            stack.pop()
            ans += len(stack)
        else:
            if len(stack) > 0:
                ans += 1
                stack.pop()
print(ans)

