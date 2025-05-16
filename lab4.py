#Task 0
def biggerNum(mas):
    res = []
    for i in range(1, len(mas)):
        if mas[i] > mas[i-1]:
            res.append(mas[i])
    return res

#Task 1
def minimax(mas):
    if not mas:
        return []

    min_val = min(mas)
    max_val = max(mas)

    min_index = mas.index(min_val)
    max_index = mas.index(max_val)

    new_mas = mas
    new_mas[min_index], new_mas[max_index] = new_mas[max_index], new_mas[min_index]

    return new_mas

#Task 2
def common_values(mas1, mas2):
    set1 = set(mas1)
    set2 = set(mas2)
    common = set1 & set2
    return len(common)

#Task 3 (через словарь)
def repeat_strings(strings):
    count_dict = {}
    for s in strings:
        if s in count_dict:
            count_dict[s] += 1
        else:
            count_dict[s] = 1

    result = list(count_dict.values())
    if len(result) == 1:
        return f"{result[0]}."
    else:
        return " ".join(map(str, result)) + "."