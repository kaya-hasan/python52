

def fibonacci():
    # generator
    a = 1
    b = 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


# generator = fibonacci()
# iterator = iter(generator)
# print(next(iterator))  # 1
# print(next(iterator))  # 1
# print(next(iterator))  # 2
# print(next(iterator))  # 3
# print(next(iterator))  # 5
# print(next(iterator))  # 8

for sayi in fibonacci():
    if sayi > 1000000:
        break
    print(sayi)
