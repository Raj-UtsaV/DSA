"""Reusable reference: multiple independent stacks."""

class NStacks:
 def __init__(self,count,capacity=None):self.stacks=[[] for _ in range(count)];self.capacity=capacity
 def push(self,value,index):
  if self.capacity is not None and sum(map(len,self.stacks))>=self.capacity:return False
  self.stacks[index].append(value);return True
 def pop(self,index):return self.stacks[index].pop() if self.stacks[index] else -1
