import sys
left = list(input())
right = []
trial = int(input())
for i in range(trial):
    order = sys.stdin.readline().split()
    if order[0] == "P":
        left.append(order[1])
    elif order[0] == "L" and left:
        right.append(left.pop())
    elif order[0] == "D" and right:
        left.append(right.pop())
    elif order[0] == "B" and left:
        left.pop()
print("".join(left + list(reversed(right))))