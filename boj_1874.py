#import sys
#input = sys.stdin.readline

check_point = 1
stack = list()
ans = list()
trial = int(input())
flag = False
for i in range(trial):
    num = int(input())
    if check_point <= num:
        while(1):
            stack.append(check_point)
            ans.append('+')
            check_point += 1
            if check_point > num:
                stack.pop()
                ans.append('-')
                break
    else:
        if len(stack) == 0:
            flag = True
            break
        if stack[-1] > num:
            while(1):
                stack.pop()
                ans.append('-')
                if stack[-1] == num:
                    stack.pop()
                    ans.append('-')
                    break
        elif stack[-1] == num:
            stack.pop()
            ans.append('-')
        else:
            flag = True
            break
if flag:
    print('NO')
else:
    print('\n'.join(ans))
