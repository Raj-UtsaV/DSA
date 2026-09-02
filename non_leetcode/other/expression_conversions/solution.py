"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Prefix and Postfix Expression Conversions
Platform: Other
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Stack, Expression Parsing
Canonical URL: Unresolved
"""

def postfix_to_infix(expr):
 stack=[]
 for ch in expr:stack.append(f"({stack.pop(-2)}{ch}{stack.pop()})" if ch in '+-*/^' else ch)
 return stack[-1]
def prefix_to_infix(expr):
 stack=[]
 for ch in reversed(expr):stack.append(f"({stack.pop()}{ch}{stack.pop()})" if ch in '+-*/^' else ch)
 return stack[-1]
