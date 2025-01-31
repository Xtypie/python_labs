n = int(input())
a = [1]
for i in range(n):
    print(a)
    a = [sum(x) for x in zip([0] + a, a + [0])]

