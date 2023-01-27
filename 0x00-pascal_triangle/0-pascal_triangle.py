#!/usr/bin/python3
"""Pascal Triangle
"""

def pascal_triangle(n):
    """Return a list of list of integers representing the
    Pascal triangle
    """
    if n < 1:
        return []
    triangle = [[1], [1, 1]]
    if n == 1:
        return triangle[:1]
    if n == 2:
        return triangle
    for level in range(2,n):
        prev = triangle[-1]
        int_list = [prev[0]]
        i = 1
        while i < len(prev):
            int_list.append(prev[i] + prev[i-1])
            i += 1
        int_list.append(1)
        triangle.append(int_list)
    return triangle
