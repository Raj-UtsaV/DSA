"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Reverse a Stack Using Recursion
Platform: GeeksforGeeks
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Stack, Recursion
Canonical URL: https://www.geeksforgeeks.org/problems/reverse-a-stack/1
"""

def reverse_stack(stack):
 def bottom(value):
  if not stack:stack.append(value);return
  top=stack.pop();bottom(value);stack.append(top)
 if stack:
  top=stack.pop();reverse_stack(stack);bottom(top)
 return stack
