"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Floor and Ceil in Sorted Array
Platform: GeeksforGeeks
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Binary Search
Canonical URL: https://www.geeksforgeeks.org/problems/ceil-the-floor2802/1
"""

from bisect import bisect_left, bisect_right
def floor_and_ceil(values,target):
 left=bisect_left(values,target);right=bisect_right(values,target)
 return (values[right-1] if right else -1, values[left] if left<len(values) else -1)
