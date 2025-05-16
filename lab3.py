s = input(str())
se = ''

m = 0

while m != len(s) - 1:
    k = m + 1
    while s[m] == s[k]:
        k += 1
    se += s[m] + str(k - m)
