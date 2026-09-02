"""Reusable reference: basic array searching and transformations."""

def linear_search(values,target):
 try:return values.index(target)
 except ValueError:return -1
def minimum_and_maximum(values):return min(values),max(values)
def reversed_array(values):return list(reversed(values))
def is_sorted(values):return all(a<=b for a,b in zip(values,values[1:]))
