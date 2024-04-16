import sys
input = sys.stdin.readline
string = list(input())
cursor = len(string)
trial = int(input())
for i in range(trial):
    order = input().split()
    if len(order) > 1:
        string.insert(cursor, order[1])
        cursor += 1
    else:
        if order[0] == 'L' and cursor != 0:
            cursor -= 1
        elif order[0] == 'D' and cursor != len(string):
            cursor += 1
        elif order[0] == 'B' and cursor != 0:
            string.pop(cursor - 1)
            cursor -= 1
    #print('cursor: ', cursor)

print(''.join(string))

