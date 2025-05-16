#Task 1
def multipl():
    with open('input.txt', 'r') as f:
        nums = list(map(int, f.read().split()))
    result = 1
    for n in nums:
        result *= n

    with open('output.txt', 'r') as f:
        f.write(str(result))

#Task 2
def natur():
    with open('nums.txt', 'r') as f:
        nums = []
        for s in f.readlines():
            nums.append(int(s))
    nums.sort()
    with open('output2.txt', 'w') as f:
        for n in nums:
            f.write(f'{n}\n')

#Task 3
def child():
    with open('kid.txt', 'r') as f:
        kid = []
        for s in f:
            data = s.strip().split()
            surname, name, age = data
            kid.append((surname, name, int(age)))

    young = min(kid, key = lambda x: x[2])
    old = max(kid, key = lambda x : x[2])

    with open('old.txt', 'w') as f:
        f.write(f'{old[0]} {old[1]} {old[2]}')
    with open('young.txt', 'w') as f:
        f.write(f'{young[0]} {young[1]} {young[2]}')

multipl()
natur()
child()





