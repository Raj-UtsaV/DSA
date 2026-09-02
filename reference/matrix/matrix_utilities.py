"""Reusable reference: basic matrix traversal helpers."""

def linear_search(matrix,target):return any(target in row for row in matrix)
def largest_row_sum(matrix):return max(range(len(matrix)),key=lambda row:sum(matrix[row])) if matrix else -1
def rotated_clockwise(matrix):return [list(row) for row in zip(*matrix[::-1])]
