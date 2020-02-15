"""
Hila Daniel.
11th grade.
Write a function which gets two matrices in suitable sizes.
The function returns the result of the multiplication between them.
Note: Multiplication of two matrices A and B is defined
only if the number of columns in A is equal to the number of rows in B.
"""


import numpy as np


def newMatrix(rows, columns):
    """
    The function creates new TD (Two-dimensional) array according to the parameters it gets.
    The function puts zero in the new array's values.
    parm rows: Num of rows
    type rows: int
    parm columns: Num of columns
    type columns: int
    :return New zeroed array
    :rtype  (TD) array
    """
    return np.zeros((rows,columns))


def mulMatrices(x,y):
    """
    The function calculates the multiplication between the two matrices it gets.
    parm x: Matrix A
    type x: (TD) array
    param y: Matrix B
    type y: (TD) array
    :return Result array
    :rtype (TD) array
    """
    # len(x) = num of rows in the result array
    # len(y[0]) = num of columns in the result array
    result = newMatrix(len(x), len(y[0]))
    for r in range(len(x)): # range[len(x)] - creates a list whose size is the number of rows in matrix x
                            # the goal: to go through every row in matrix x
        for c in range(len(y[0])):# range[len(x)] - creates a list whose size is the number of columns in matrix y
                                  # the goal: to go through every column in matrix y
            for n in range(len(x[0])):# range[len(x[0])] - creates a list whose size is the number of columns in matrix x.
                                      # reminder: len(x[0]) = len(y) (num of columns in x equals to num of rows in y)
                result[r][c] = result[r][c] + (x[r][n] * y[n][c])
    return result


def main():
    # 2x3 matrix
    x = np.array([[5, 8, 7],
                 [1, 2, 3]])
    # 3x4 matrix
    y = np.array([[1, 2, 3, 6],
                 [3, 4, 8, 2],
                 [5, 6, 1, 0]])
    mul = mulMatrices(x,y)



if __name__ == '__main__':
    main()