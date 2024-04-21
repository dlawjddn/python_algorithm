origin = input()
ans = list()
for i in range(len(origin)):
    ans.append(origin[i:len(origin)])
print("\n".join(sorted(ans)))