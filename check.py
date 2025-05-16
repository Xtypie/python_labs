s = input(str())
se = ''

m = 0
c = 0

for k in range(m, len(s) - 1):
    if s[m] == s[k]:
        c += 1
        continue
    if s[m] != s[k]:
        se += str(s[m]) + str(c)
        c = 0
        m = k + 1

print(se)


