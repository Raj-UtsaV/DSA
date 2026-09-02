"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Sort a Stack
Platform: GeeksforGeeks
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Stack, Recursion
Canonical URL: https://www.geeksforgeeks.org/problems/sort-a-stack/1
"""

"""
Given a stack, the task is to sort it such that
the top of the stack has the greatest element.
"""

#!IDEA:
"""

take out last element and sort rest of the stack
after yot got the rest stak sorted the put the last value at the proper place

do it recursively


"""

class Solution:

    def sorted_insert(self,stack,val):
        if not stack or val>stack[-1]:
            stack.append(val)
            return

        top = stack.pop()
        self.sorted_insert(stack,val)
        stack.append(top)

    def Sorted(self, s):
        if not s:
            return

        top = s.pop()
        self.Sorted(s)
        self.sorted_insert(s,top)


if __name__ == "__main__":
    stack = [3, 1, 4, 2, 5]
    print("Original stack:", stack)
    sol=Solution()
    sol.Sorted(stack)
    print("Sorted stack:", stack)