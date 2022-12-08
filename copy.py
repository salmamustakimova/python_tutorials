def my_dist(a, b):
    def recursive(i, j):
        if i == 0 or j == 0:
            # если одна из строк пустая, то расстояние до другой строки - ее длина
            # т.е. n вставок
            return max(i, j)
        elif a[i - 1] == b[j - 1]:
            # если оба последних символов одинаковые, то съедаем их оба, не меняя расстояние
            return recursive(i - 1, j - 1)
        else:
            # иначе выбираем минимальный вариант из трех
            return 1 + min(
                recursive(i, j - 1),  # удаление
                recursive(i - 1, j),   # вставка
                recursive(i - 1, j - 1)  # замена
            )
    return recursive(len(a), len(b))
