"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Page Faults in LRU
Platform: GeeksforGeeks
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: LRU Simulation
Canonical URL: https://www.geeksforgeeks.org/problems/page-faults-in-lru5603/1
"""

from collections import OrderedDict
def page_faults(pages,capacity):
 cache=OrderedDict();faults=0
 for page in pages:
  if page in cache:cache.move_to_end(page)
  else:
   faults+=1
   if len(cache)==capacity:cache.popitem(last=False)
   cache[page]=None
 return faults
