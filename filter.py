# -*- coding: utf-8 -*-
"""
Hila Daniel.
11th grade.
A solution to the question of 28.2.2020.
"""

import numpy as np

def main():
    #זימון ראשון
    # 8x8 matrix
    a = np.array([[0, 0, 0, 1, 1, 0, 0, 0],
                  [0, 0, 0, 1, 1, 0, 0, 0],
                  [0, 0, 0, 1, 1, 0, 0, 0],
                  [0, 0, 0, 1, 1, 0, 0, 0],
                  [0, 0, 0, 1, 1, 0, 0, 0],
                  [0, 0, 0, 1, 1, 0, 0, 0],
                  [0, 0, 0, 1, 1, 0, 0, 0],
                  [0, 0, 0, 1, 1, 0, 0, 0]])
    my_filter = random_filter()   
    new_array = mul(a, my_filter)
    print(np.matrix(new_array))
    
#זימון שני והלאה
    while len(my_filter) <= len(new_array):
        my_filter = random_filter()         
        new_array = mul(new_array, my_filter)
        print(np.matrix(new_array))   
    
     
def random_filter():
    """
    The function randoms positive double numbers in the range 0.0 to 5.0
    to 3X3 (TD) array.
    :return random 3X3 (TD) array.
    :rtype (TD) array.
    """
    filt = np.random.rand(3,3)
    for r in range(len(filt)):
        for c in range(len(filt[0])):
            filt[r][c] = filt[r][c] * 5
    return filt
    

def self_sum(matrix):
    """
    The function calculates the sum of the numners in the matrix it gets.
    parm matrix: Matrix.
    type matrix: (TD) array.
    :return sum as explained above.
    :rtype int.
    """
    final_sum = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            final_sum += matrix[r][c] 
    return final_sum        
    

def mul(a, my_filter):
    """
    The function calculates the multiplication of the two matrices
    it gets, as asked in the question.
    param a: Given array, maximum size is 8X8.
    param my_filter: random 3X3 (TD) array.
    :return Result_array.
    :rtype (TD) array.
    """
    rows = len(a) - 2 #rows: Num of rows in result_array.
    columns = len(a[0]) - 2 #columns: Num of columns in result_array.
    result_array = np.zeros((rows,columns))
    for r in range(len(result_array)):
        for c in range(len(result_array[0])):
            cube = a[r:r+3,c:c+3]
            mul_matrix = np.dot(cube, my_filter)
            sum0 = self_sum(mul_matrix)
            result_array[r][c] = sum0
    return result_array


if __name__ == '__main__':
    main()   
    
    
    
    
    
    
    