"""Reusable reference: iterative and recursive binary search."""

def binary_search(values,target):
 left,right=0,len(values)-1
 while left<=right:
  mid=(left+right)//2
  if values[mid]==target:return mid
  if values[mid]<target:left=mid+1
  else:right=mid-1
 return -1
def recursive_binary_search(values,target,left=0,right=None):
 right=len(values)-1 if right is None else right
 if left>right:return -1
 mid=(left+right)//2
 return mid if values[mid]==target else recursive_binary_search(values,target,mid+1,right) if values[mid]<target else recursive_binary_search(values,target,left,mid-1)
