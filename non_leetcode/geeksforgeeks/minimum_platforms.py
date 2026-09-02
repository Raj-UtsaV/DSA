"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Minimum Platforms
Platform: GeeksforGeeks
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Sorting, Two Pointers
Canonical URL: https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1
"""

def minimum_platforms(arrival,departure):
 arrival.sort();departure.sort();i=j=current=answer=0
 while i<len(arrival):
  if arrival[i]<=departure[j]:current+=1;answer=max(answer,current);i+=1
  else:current-=1;j+=1
 return answer
