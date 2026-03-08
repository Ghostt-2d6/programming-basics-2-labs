def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        c = a + b
        a = b
        b = c