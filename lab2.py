def SerTriangle(iter, size):
    tr = [[" " for _ in range(size)] for _ in range(size)]

    def print_tr(x, y, iter):

        if (iter == 0):
            tr[y][x] = "*"
        else:
            new_iter = iter - 1
            height = 2 ** new_iter

            print_tr(x, y, new_iter)
            print_tr(x - height // 2, y + height, new_iter)
            print_tr(x + height // 2, y + height, new_iter)

    print_tr(size // 2, 0, iter)

    for i in tr:
        print("".join(i))

#Task 1

n = int(input())
a = [1]
for i in range(n):
    print(a)
    a = [sum(x) for x in zip([0] + a, a + [0])]

#Task 2

iter = 6
size = 2 ** iter
SerTriangle(iter, size)


