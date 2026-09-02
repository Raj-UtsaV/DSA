"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Infix to Postfix
Platform: GeeksforGeeks
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Stack, Expression Parsing
Canonical URL: https://www.geeksforgeeks.org/problems/infix-to-postfix-1587115620/1
"""

def infix_to_postfix(expression):
 precedence={'^':3,'*':2,'/':2,'+':1,'-':1};stack=[];out=[]
 for ch in expression:
  if ch.isalnum():out.append(ch)
  elif ch=='(':stack.append(ch)
  elif ch==')':
   while stack and stack[-1]!='(':out.append(stack.pop())
   stack.pop()
  else:
   while stack and stack[-1]!='(' and (precedence[stack[-1]]>precedence[ch] or precedence[stack[-1]]==precedence[ch] and ch!='^'):out.append(stack.pop())
   stack.append(ch)
 return ''.join(out+stack[::-1])
