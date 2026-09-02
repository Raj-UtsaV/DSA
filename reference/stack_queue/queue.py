"""Reusable reference: array-backed queue."""

from collections import deque
class Queue:
 def __init__(self):self._items=deque()
 def push(self,value):self._items.append(value)
 def pop(self):return self._items.popleft()
 def front(self):return self._items[0]
 def empty(self):return not self._items
 def __len__(self):return len(self._items)
