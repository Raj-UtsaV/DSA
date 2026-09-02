"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Maximum Occurring Character
Platform: Other
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Frequency Counting
Canonical URL: Unresolved
"""

from collections import Counter
def maximum_occurring_character(text):
 counts=Counter(text.lower());return min(counts,key=lambda ch:(-counts[ch],ch)) if counts else None
