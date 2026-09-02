"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Job Sequencing Problem
Platform: GeeksforGeeks
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Greedy Scheduling
Canonical URL: https://www.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1
"""

def job_sequencing(jobs):
 slots=[False]*(max((d for _,d,_ in jobs),default=0)+1);count=profit=0
 for _,deadline,value in sorted(jobs,key=lambda x:x[2],reverse=True):
  for t in range(deadline,0,-1):
   if not slots[t]:slots[t]=True;count+=1;profit+=value;break
 return count,profit
