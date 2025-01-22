# a = int(input())
# b = int(input())
# c = int(input())
# list = [a, b, c]
# mx, mn = None, None
# for i in list:
#     if mx is None or mx < i: mx = i
#     if mn is None or mn > i: mn = i
# print("max =", mx, "min =", mn)


#Task 2.1
n = int(input())
s = ''

for i in range(1, n + 1):
    s += str(i)
for i in range(n):
    print(s)
    s = s[:-1]





