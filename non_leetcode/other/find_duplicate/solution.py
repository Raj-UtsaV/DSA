"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Find a Duplicate Element
Platform: Other
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Array, Frequency Counting
Canonical URL: Unresolved
"""

def find_duplicate(values):
 seen=set()
 for value in values:
  if value in seen:return value
  seen.add(value)
 return None
