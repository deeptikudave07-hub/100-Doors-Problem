n = [0 for i in range(101)]

for i in range(1, len(n) + 1):
    for j in range(1, len(n), i):
        if n[j] == 0:
            n[j] = 1
        else:
            n[j] = 0

print(n.count(1))
print(n)
