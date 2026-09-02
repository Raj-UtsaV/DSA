"""Reusable reference: doubly linked-list helpers."""

class Node:
 def __init__(self,data):self.data=data;self.prev=self.next=None
class DoublyLinkedList:
 def __init__(self):self.head=self.tail=None
 def append(self,value):
  node=Node(value)
  if not self.head:self.head=self.tail=node
  else:node.prev=self.tail;self.tail.next=node;self.tail=node
 def values(self):
  out=[];node=self.head
  while node:out.append(node.data);node=node.next
  return out
 def reverse(self):
  node=self.head
  while node:node.prev,node.next=node.next,node.prev;node=node.prev
  self.head,self.tail=self.tail,self.head
