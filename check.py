def sierpinski_triangle(iter, size):
    # Создаем пустое поле
    triangle = [[" " for _ in range(size)] for _ in range(size)]

    def draw_triangle(x, y, iter):
        if iter == 0:
            triangle[y][x] = "*"
        else:
            # Вычисляем новые размеры
            new_order = iter - 1
            height = 2 ** new_order

            # Рисуем три треугольника
            draw_triangle(x, y, new_order)  # верхний треугольник
            draw_triangle(x - height // 2, y + height, new_order)  # левый треугольник
            draw_triangle(x + height // 2, y + height, new_order)  # правый треугольник

    # Начинаем с верхнего треугольника
    draw_triangle(size // 2, 0, iter)

    # Вывод результата
    for line in triangle:
        print("".join(line))


# Задаем порядок треугольника
iter = 3  # Измените на нужный вам порядок
size = 2 ** iter  # Размерность треугольника
sierpinski_triangle(iter, size)