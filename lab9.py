import numpy as np
#Task 1
def matr(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            row = list(map(int, line.strip().split()))
            matrix.append(row)

    total_sum = 0
    min_element = matrix[0][0]
    max_element = matrix[0][0]

    for row in matrix:
        for num in row:
            total_sum += num
            if num < min_element:
                min_element = num
            if num > max_element:
                max_element = num

    return total_sum, min_element, max_element

#Task2
def rle_encode_python(x):
    if not x:
        return [], []

    values = []
    counts = []
    current_val = x[0]
    count = 1

    for val in x[1:]:
        if val == current_val:
            count += 1
        else:
            values.append(current_val)
            counts.append(count)
            current_val = val
            count = 1

    values.append(current_val)
    counts.append(count)

    return values, counts

#Task 3
np.random.seed(42)
array = np.random.randn(10, 4)

min_val = np.min(array)
max_val = np.max(array)
mean_val = np.mean(array)
std_val = np.std(array)

first_5_rows = array[:5, :]

print(array)
print(f"minimal value: {min_val:.4f}")
print(f"maximal value: {max_val:.4f}")
print(f"average value: {mean_val:.4f}")
print(f"std value: {std_val:.4f}")
print("\n5 rows:")
print(first_5_rows)

#Task 4

def max_val_after0(x):
    zero_indices = np.where(x[:-1] == 0)[0]

    elements_after_zero = x[zero_indices + 1]
    return np.max(elements_after_zero)

#Task 5 не понимаю как делать, извините пожалуйста :\

#Task 6
a = np.array([[1,2,3],
             [4,5,6],
             [7,8,9],
             [10,11,12]])

a[[0,2]] = a[[2,0]]

print(a)

#Task 7
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

species = iris[:, -1]

unique_species, counts = np.unique(species, return_counts=True)

for species, count in zip(unique_species, counts):
    print(f"{species.decode('utf-8')}: {count}")

#Task 8
arr = np.array([0, 1, 2, 0, 0, 4, 0, 6, 9])
ind = np.nonzero(arr)[0]

print(ind)