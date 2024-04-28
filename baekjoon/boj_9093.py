trial = int(input())

for i in range(trial):
    string = input().split()
    for j in range(0, len(string)):
        print(string[j][::-1], end=" ")
    print()