#!/usr/bin/python3
"""Module to multiply two matrices using NumPy"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Function that multiplies two matrices using NumPy
    
    Args:
        m_a (list of lists of int/float): first matrix
        m_b (list of lists of int/float): second matrix

    Returns:
        list of lists: result of matrix multiplication
    """
    # Validate types
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    # Validate elements
    for row in m_a:
        if not all(isinstance(el, (int, float)) for el in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(el, (int, float)) for el in row):
            raise TypeError("m_b should contain only integers or floats")
    # Validate rectangular
    row_len_a = len(m_a[0])
    if any(len(row) != row_len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    row_len_b = len(m_b[0])
    if any(len(row) != row_len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    # Validate multiplication compatibility
    if row_len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    # Use NumPy to multiply matrices
    result = np.matmul(np.array(m_a), np.array(m_b))
    return result.tolist()
