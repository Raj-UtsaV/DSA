"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Longest Subarray with Sum K
Platform: Code360
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Sliding Window, Prefix Sum
Canonical URL: https://www.naukri.com/code360/problems/longest-subarray-with-sum-k_6682399
"""

def longest_subarray_with_sum_k(values,k):
 left=total=answer=0
 for right,x in enumerate(values):
  total+=x
  while left<=right and total>k:total-=values[left];left+=1
  if total==k:answer=max(answer,right-left+1)
 return answer
