"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Number of NGEs to the Right
Platform: GeeksforGeeks
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Array, Queries
Canonical URL: https://www.geeksforgeeks.org/problems/number-of-nges-to-the-right/1
"""

def count_nges(values,indices):return [sum(x>values[i] for x in values[i+1:]) for i in indices]
