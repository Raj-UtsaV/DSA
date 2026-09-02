"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Fractional Knapsack
Platform: GeeksforGeeks
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Greedy, Sorting
Canonical URL: https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1
"""

def fractional_knapsack(capacity,items):
 total=0.0
 for value,weight in sorted(items,key=lambda x:x[0]/x[1],reverse=True):
  take=min(capacity,weight);total+=take*value/weight;capacity-=take
  if capacity==0:break
 return total
