"""Reusable reference: singly linked-list helpers."""

class Node:
 def __init__(self,data,next=None):self.data,self.next=data,next
class SinglyLinkedList:
 def __init__(self,values=()):
  self.head=None
  for value in reversed(list(values)):self.head=Node(value,self.head)
 def append(self,value):
  node=Node(value)
  if not self.head:self.head=node;return
  tail=self.head
  while tail.next:tail=tail.next
  tail.next=node
 def values(self):
  out=[];node=self.head
  while node:out.append(node.data);node=node.next
  return out
 def reverse(self):
  previous=None;node=self.head
  while node:node.next,previous,node=previous,node,node.next
  self.head=previous
