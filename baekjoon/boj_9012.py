trial = int(input())
for i in range(trial):
    brackets = input()
    stack = list()
    flag = False
    for j in range(len(brackets)):
        if brackets[j] == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                flag = True
                break
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    flag = True
                    break
    if flag:
        print('NO')
    else:
        if len(stack) != 0:
            print('NO')
        else:
            print('YES')