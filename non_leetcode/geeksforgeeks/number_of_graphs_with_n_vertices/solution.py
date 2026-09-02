"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Number of Graphs with N Vertices
Platform: GeeksforGeeks
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Combinatorics, Modular Exponentiation
Canonical URL: https://www.geeksforgeeks.org/problems/number-of-graphs-with-n-vertices/1
"""

def count_graphs(n,mod=1_000_000_007):return pow(2,n*(n-1)//2,mod)
