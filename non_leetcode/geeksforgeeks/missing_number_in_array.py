"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Missing Number in Array
Platform: GeeksforGeeks
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Array, Arithmetic
Canonical URL: https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1
"""

def missing_number(values):return (len(values)+1)*(len(values)+2)//2-sum(values)
