"""Reusable reference: common recursion patterns."""

def fast_power(base,exponent):
 if exponent==0:return 1
 half=fast_power(base,exponent//2);return half*half*(base if exponent%2 else 1)
def string_subsequences(text):
 out=[]
 def visit(i,current):
  if i==len(text):out.append(current);return
  visit(i+1,current);visit(i+1,current+text[i])
 visit(0,'');return out
def reverse_string(text):return text if len(text)<2 else reverse_string(text[1:])+text[0]
