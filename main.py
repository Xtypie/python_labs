# #Task 1
#
# a = int(input())
# b = int(input())
# c = int(input())
# list = [a, b, c]
# mx, mn = None, None
# for i in list:
#     if mx is None or mx < i: mx = i
#     if mn is None or mn > i: mn = i
# if a == b == c:
#     print("все числа одинаковы")
# print("max =", mx, "min =", mn)
#
#
# #Task 2.1
#
n = int(input())
s = ''

for i in range(1, n + 1):
    s += str(i)
for i in range(n):
    print(s)
    if ('10' in s):
        s = s[:-2]
    else:
        s = s[:-1]


#Task 2.2

# i = int(input())
# s2 = ''
#
# for n in range(1, i + 1):
#     s2 += str(n)
# for i in range(n):
#     print(s2[::-1] + s2[1:])
#     s = s2[:-1]






