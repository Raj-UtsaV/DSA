"""Reusable reference: array-backed and linked conceptual stack."""

class Stack:
 def __init__(self):self._items=[]
 def push(self,value):self._items.append(value)
 def pop(self):return self._items.pop()
 def top(self):return self._items[-1]
 def empty(self):return not self._items
 def __len__(self):return len(self._items)
