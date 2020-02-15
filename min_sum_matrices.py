"""
Hila Daniel.
11th grade.
Write a function which gets two matrices and 
returns the minimal sum of them.
"""


import numpy as np


def find_min_num(a, b):
    """
    The function finds the minimum number of the parameters it gets.
    parm a: First num
    type a: int
    parm b: Second num
    type b: int
    :return minimum of a and b
    :rtype  int
    """
    return min([a, b])


def find_min_sum_matrices(x, y):
    """
    The function calculates the minimal sum of the two matrices it gets.
    parm x: Matrix A
    type x: (TD) array
    param y: Matrix B
    type y: (TD) array
    :return Result array
    :rtype (TD) array
    """
    min_rows = find_min_num(len(x), len(y))
    min_columns = find_min_num(len(x[0]),len(y[0]))
    min_x = x[0:min_rows,0:min_columns] 
    min_y = y[0:min_rows,0:min_columns] 
    return min_x + min_y 
    

def main():
    a = np.array([[1, 2, 3, 1],
                  [4, 5, 6, 3],
                  [7, 8, 9, 5],
                  [10, 11, 12, 2],
                  [13, 14, 15, 0],
                  [16, 17, 18, 6],
                  [19, 20, 21, 2]])

    b = np.array([[1, 2, 3, 4, 5, 6],
                  [8, 9, 10, 11, 12, 13],
                  [14, 15, 16, 17, 18, 19]])
    
    result = find_min_sum_matrices(a, b)


if __name__ == '__main__':
    main()



