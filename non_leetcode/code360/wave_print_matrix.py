"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Print Matrix in Wave Form
Platform: Code360
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Matrix Traversal
Canonical URL: Unresolved
"""

def wave_print(matrix):return [matrix[row][col] for col in range(len(matrix[0])) for row in (range(len(matrix)) if col%2==0 else range(len(matrix)-1,-1,-1))]
