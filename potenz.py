def potenz(a, b):
    p = 1
    for i in range(b):
        p = p * a
    return a

print(potenz(3, 4))
print(potenz(3, 5))