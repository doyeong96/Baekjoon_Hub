n, m = map(int, input().split())
li = []
S = 0
for i in range(m):
    a = i + 1
    while a != 0:
        li.append(i + 1)
        a -= 1
print(sum(li[n-1:m]))