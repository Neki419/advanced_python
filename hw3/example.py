import numpy as np
from matrix import Matrix
from mixins import ArrayWrapper

# np.random.seed(0)

# m1, m2 = Matrix(np.random.randint(0, 10, (10, 10))), Matrix(np.random.randint(0, 10, (10, 10)))

# with open('hw3/matrix+.txt', 'w', encoding='utf-8') as file:
#     file.write('Addition\n')
#     file.write(repr(m1 + m2))
# with open('hw3/matrix*.txt', 'w', encoding='utf-8') as file:
#     file.write('Multiplication\n')
#     file.write(repr(m1 * m2))
# with open('hw3/matrix@.txt', 'w', encoding='utf-8') as file:
#     file.write('Matrix multiplication\n')
#     file.write(repr(m1 @ m2))

# a = ArrayWrapper([[1, 2, 3], [4, 5, 6]])
# a.write('hw3/mixins_artifacts.txt')
# b = ArrayWrapper([[1, 3, 5], [7, 9, 11]])
# b.write('hw3/mixins_artifacts.txt')
# c = a + b
# c.write('hw3/mixins_artifacts.txt')
# d = 2 * c
# d.write('hw3/mixins_artifacts.txt')
# e = d * c
# e.write('hw3/mixins_artifacts.txt')

#Хеш-функция класса Matrix просто находит сумму всеъ элементов, соотвественно достаточно взять 4 элемента и поставить их в матрицах 2 x 2 в разном порядке

a = Matrix([[1, 2], [3, 4]])
c = Matrix([[4, 3], [2, 1]])

print(f'A is\n{a}')
print(f'C is\n{c}')
print(f'hash A: {hash(a)}')
print(f'hash C: {hash(c)}')

print(f'A != C is {a != c}')

b = d = Matrix([[2, 1], [4, 3]])

print(f'B is\n{b}')
print(f'D is\n{d}')

print(f'A @ B is\n{a @ b}')
print(f'C @ D is\n{c @ d}')

print(f'(hash(A) == hash(C)) and (A != C) and (B == D) and (A @ B != C @ D) is\
       {(hash(a) == hash(c)) and (a != c) and (b == d) and (a @ b != c @ d)}')

with open("hw3/A.txt", "w", encoding="utf-8") as file:
    file.write(str(a))

with open("hw3/B.txt", "w", encoding="utf-8") as file:
    file.write(str(b))

with open("hw3/C.txt", "w", encoding="utf-8") as file:
    file.write(str(c))

with open("hw3/D.txt", "w", encoding="utf-8") as file:
    file.write(str(d))

with open("hw3/AB.txt", "w", encoding="utf-8") as file:
    file.write(str(a @ b))

with open("hw3/CD.txt", "w", encoding="utf-8") as file:
    file.write(str(c @ d))

with open("hw3/hash.txt", "w", encoding="utf-8") as file:
    file.write(f'hash AB is {str(hash(a @ b))}\n')
    file.write(f'hash CD is {str(hash(c @ d))}\n')