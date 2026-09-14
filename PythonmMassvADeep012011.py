
# import random

import random


def main():
    # Ввод размера массива
    try:
        N = int(input("Введите размерность массива N: "))
        if N <= 0:
            print("Размер массива должен быть положительным числом.")
            return
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")
        return

    # Создание и заполнение массива случайными числами
    A = [random.randint(-10, 10) for _ in range(N)]

    print("Исходный массив:")
    print(' '.join(map(str, A)))

    # Поиск индексов минимального и максимального элементов
    min_index = 0
    max_index = 0

    for i in range(1, N):
        if A[i] < A[min_index]:
            min_index = i
        if A[i] > A[max_index]:
            max_index = i

    print(f"Минимальный элемент A[{min_index}] = {A[min_index]}")
    print(f"Максимальный элемент A[{max_index}] = {A[max_index]}")

    # Определение границ интервала
    start = min(min_index, max_index) + 1
    end = max(min_index, max_index) - 1

    # Проверка, есть ли элементы между ними
    if start > end:
        print("Между минимальным и максимальным элементами нет других элементов.")
        return

    # Вычисление суммы отрицательных элементов
    sum_negative = 0
    negative_elements = []
    
    for i in range(start, end + 1):
        if A[i] < 0:
            negative_elements.append(A[i])
            sum_negative += A[i]

    if negative_elements:
        print("Отрицательные элементы между ними:")
        print(' '.join(map(str, negative_elements)))
        print(f"Сумма отрицательных элементов между минимальным и максимальным: {sum_negative}")
    else:
        print("Отрицательных элементов между минимальным и максимальным не найдено.")

if __name__ == "__main__":
    main()
