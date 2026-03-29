#!/usr/bin/python3
"""Matrix multiplication module
"""


def matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices

    Args:
        m_a (list of lists of int/float): first matrix
        m_b (list of lists of int/float): second matrix

    Returns:
        list of lists of int/float: matrix product

    Raises:
        TypeError, ValueError: on invalid input
    """
    # Validate m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Validate m_a and m_b are list of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Validate not empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # Validate elements are int or float
    if not all(isinstance(el, (int, float)) for row in m_a for el in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(el, (int, float)) for row in m_b for el in row):
        raise TypeError("m_b should contain only integers or floats")

    # Validate rectangular shape
    row_len_a = len(m_a[0])
    if not all(len(row) == row_len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    row_len_b = len(m_b[0])
    if not all(len(row) == row_len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Validate multiplication compatibility
    if row_len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform multiplication
    result = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            sum_prod = 0
            for k in range(len(m_b)):
                sum_prod += m_a[i][k] * m_b[k][j]
            new_row.append(sum_prod)
        result.append(new_row)

    return result
