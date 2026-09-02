"""Reusable reference: comparison sorting algorithms."""

def selection_sort(values):
 values=list(values)
 for i in range(len(values)):
  j=min(range(i,len(values)),key=values.__getitem__);values[i],values[j]=values[j],values[i]
 return values
def bubble_sort(values):
 values=list(values)
 for end in range(len(values)-1,0,-1):
  changed=False
  for i in range(end):
   if values[i]>values[i+1]:values[i],values[i+1]=values[i+1],values[i];changed=True
  if not changed:break
 return values
def insertion_sort(values):
 values=list(values)
 for i in range(1,len(values)):
  value=values[i];j=i-1
  while j>=0 and values[j]>value:values[j+1]=values[j];j-=1
  values[j+1]=value
 return values
def merge_sort(values):
 if len(values)<2:return list(values)
 mid=len(values)//2;left=merge_sort(values[:mid]);right=merge_sort(values[mid:]);out=[]
 while left and right:out.append(left.pop(0) if left[0]<=right[0] else right.pop(0))
 return out+left+right
def quick_sort(values):
 if len(values)<2:return list(values)
 pivot=values[len(values)//2]
 return quick_sort([x for x in values if x<pivot])+[x for x in values if x==pivot]+quick_sort([x for x in values if x>pivot])
