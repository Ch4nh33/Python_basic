res = []
for i in range(10):
    a = int(input())
    res.append(int(a)%42)
res = set(res)
print(len(res))
