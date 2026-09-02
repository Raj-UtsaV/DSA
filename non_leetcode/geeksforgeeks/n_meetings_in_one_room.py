"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: N Meetings in One Room
Platform: GeeksforGeeks
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Activity Selection
Canonical URL: https://www.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1
"""

def max_meetings(start,end):
 finish=float("-inf");count=0
 for stop,begin in sorted(zip(end,start)):
  if begin>finish:count+=1;finish=stop
 return count
