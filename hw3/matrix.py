import numbers
import itertools

class HashMixin:
    def __hash__(self):
        return sum(itertools.chain.from_iterable(self.matrix))
    
class EqualMixin:
    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.matrix == other.matrix
        return False

class Matrix(HashMixin, EqualMixin):

    product_cache = {}

    def __init__(self, matrix: list[list[numbers.Number]]):
        self.row_num = len(matrix)
        self.col_num = len(matrix[0])
        self.matrix = matrix

    def __repr__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])
    
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])
                
    def __add__(self, else_matrix: 'Matrix'):

        if self.row_num != else_matrix.row_num or self.col_num != else_matrix.col_num:
            raise ValueError("Matrix sizes must match for addition")
        
        return Matrix([[self.matrix[i][j] + else_matrix.matrix[i][j] for j in range(self.col_num)] for i in range(self.row_num)])
    
    def __mul__(self, else_matrix: 'Matrix'):

        if self.row_num != else_matrix.row_num or self.col_num != else_matrix.col_num:
            raise ValueError("Matrix sizes must match for multiply")
        
        return Matrix([[self.matrix[i][j] * else_matrix.matrix[i][j] for j in range(self.col_num)] for i in range(self.row_num)])
    
    def __matmul__(self, else_matrix: 'Matrix'):

        if self.col_num != else_matrix.row_num:
            raise ValueError("")
        
        result = [[0 for _ in range(else_matrix.col_num)] for _ in range(self.row_num)]

        for i in range(self.row_num):
            for j in range(else_matrix.col_num):
                for k in range(self.col_num):
                    result[i][j] += self.matrix[i][k] * else_matrix.matrix[k][j]

        matrix = Matrix(result)

        if hash(matrix) not in Matrix.product_cache:
            Matrix.product_cache[hash(matrix)] = matrix

        return Matrix(result)
    
print(hash(Matrix([[1, 2], [1, 2]])))