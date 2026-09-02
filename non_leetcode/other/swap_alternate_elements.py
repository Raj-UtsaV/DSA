"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Swap Alternate Elements
Platform: Other
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Array
Canonical URL: Unresolved
"""

def swap_alternate(values):
 for i in range(0,len(values)-1,2):values[i],values[i+1]=values[i+1],values[i]
 return values
