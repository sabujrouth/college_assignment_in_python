# Write a python program to print a 2D list in a spiral manner
def spiral_print(matrix):
    m, n = len(matrix), len(matrix[0])
    row_start, row_end = 0, m - 1
    col_start, col_end = 0, n - 1

    while row_start <= row_end and col_start <= col_end:
        # Print top row
        for i in range(col_start, col_end+1):
            print(matrix[row_start][i], end=" ")
        row_start += 1

        # Print right column
        for i in range(row_start, row_end+1):
            print(matrix[i][col_end], end=" ")
        col_end -= 1

        # Print bottom row
        if row_start <= row_end:
            for i in range(col_end, col_start-1, -1):
                print(matrix[row_end][i], end=" ")
            row_end -= 1

        # Print left column
        if col_start <= col_end:
            for i in range(row_end, row_start-1, -1):
                print(matrix[i][col_start], end=" ")
            col_start += 1

# Example usage
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
spiral_print(matrix)