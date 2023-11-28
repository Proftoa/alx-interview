def pascal_triangle(n):
    if n <= 0:
        return []  # Returns an empty list if n <= 0

    triangle = []  # Initialize the Pascal's triangle

    for i in range(n):
        row = [1]  # First element of each row is always 1
        if triangle:
            last_row = triangle[-1]  # Get the previous row
            row.extend([last_row[j] + last_row[j + 1] for j in range(len(last_row) - 1)])
            row.append(1)  # Last element of each row is always 1
        triangle.append(row)  # Add the current row to the triangle

    return triangle

