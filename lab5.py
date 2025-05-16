#Task 1
def uniqueNums(mas):
    mas_res = set(mas)
    return len(mas_res)

#Task 2
def mnozh(mas1, mas2):
    if (mas1 == mas2):
        return False
    for i in range(len(mas1)):
        if (mas1[i] not in mas2):
            return False

    return True

#Task 3
def game(n):
    cities = set()
    for i in range(n):
        city = input().strip()
        cities.add(city)

    new_city = input("Enter a new city: ").strip()

    if new_city in cities:
        print("REPEAT")
    else:
        print("OK")