def distance(a, b):
    n, m = len(a), len(b)
    if n > m:
        a, b = b, a
        n, m = m, n

    x = range(n + 1)
    for i in range(1, m + 1):
        y, x = x, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = y[j] + 1, x[j - 1] + 1, y[j - 1]
            if a[j - 1] != b[i - 1]:
                change += 1
            x[j] = min(add, delete, change)

    return x[n]
n = "ривет"


ojegov = ["привет","пока","до","свидания"]
min_word = ""
min_value = int(1000)
for word in ojegov:
    m = distance(n,word)
    if min_value > m:
        min_value = m
        min_word = word
print(min_value, min_word)

   