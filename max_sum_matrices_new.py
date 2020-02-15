"""
Hila Daniel.
11th grade.
Write a function which gets two matrices and 
returns the maximum sum of them.
"""


import numpy as np


def find_max_num(a, b):
    """
    The function finds the maximum number of the parameters it gets.
    parm a: First num
    type a: int
    parm b: Second num
    type b: int
    :return maximum of a and b
    :rtype  int
    """
    return max([a, b])


def add_row(A, num):
    """
    The function adds *num* rows to matrix A.
    parm A: Matrix
    type A: (TD) array
    parm num: how many rows to add 
    type num: int
    :return New matrix A
    :rtype  (TD) array
    """
    for i in range(num):
        new_array = np.append(A, [np.zeros(len(A[0]))], axis=0)
        A = new_array
    return A


def add_column(A, num):
    """
    The function adds *num* columns to matrix A.
    parm A: Matrix
    type A: (TD) array
    parm num: how many columns to add 
    type num: int
    :return New matrix A
    :rtype  (TD) array
    """
    for i in range(num):
        new_array = np.c_[A,np.zeros(len(A))]
        A = new_array
    return A


def find_max_sum_matrices(x, y):
    """
    The function calculates the maximum sum of the two matrices it gets.
    parm x: Matrix A
    type x: (TD) array
    param y: Matrix B
    type y: (TD) array
    :return Result array
    :rtype (TD) array
    """
    max_rows = find_max_num(len(x), len(y))
    max_columns = find_max_num(len(x[0]),len(y[0]))
    x = add_row(x, max_rows - len(x))
    y = add_row(y, max_rows - len(y))
    x = add_column(x, max_columns - len(x[0]))
    y = add_column(y, max_columns - len(y[0]))
    return x + y 
    

def main():
    # 2x3 matrix
    x = np.array([[5, 8, 7],
                 [1, 2, 3]])
    # 3x2 matrix
    y = np.array([[1, 2],
                  [3, 4],
                  [5, 6]])
    
    result = find_max_sum_matrices(x, y)


if __name__ == '__main__':
    main()



