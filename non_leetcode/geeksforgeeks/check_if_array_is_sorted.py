"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Check if an Array Is Sorted
Platform: GeeksforGeeks
Difficulty: Easy
Official Platform Topics: Not specified
Study Tags: Array
Canonical URL: https://www.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1
"""

def is_sorted(values):return all(a<=b for a,b in zip(values,values[1:]))
