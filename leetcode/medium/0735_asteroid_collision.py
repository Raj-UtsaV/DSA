"""Canonical solution metadata.

Problem Number: 735
Problem Title: Asteroid Collision
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Stack, Simulation
Study Tags: Collision Simulation
Canonical URL: https://leetcode.com/problems/asteroid-collision/
"""

class Solution:
 def asteroidCollision(self,asteroids):
  stack=[]
  for a in asteroids:
   while stack and a<0<stack[-1]:
    if stack[-1]<-a:stack.pop();continue
    if stack[-1]==-a:stack.pop()
    break
   else:stack.append(a)
  return stack
