"""
Given an integer N , Print all binary strings of size N which do not contain consecutive 1s.

A binary string is that string which contains only 0 and 1.


Example 1:

Input:
N = 3
Output:
000 , 001 , 010 , 100 , 101
Explanation:
None of the above strings contain consecutive 1s. "110" is not an answer as it has '1's occuring consecutively. 


"""

#!IDEA
"""
use recursion to find all the substring 


"""

class Solution:

    def find(self,str,ans,n):
        if len(str) == n:
            ans.append(str)
            return
        
        include_0 = self.find(str+'0',ans,n) 
        if str == "" or str[-1] != '1':
            include_1 = self.find(str+'1',ans,n)

    def generateBinaryStrings(self, n):
        ans = []
        self.find("",ans,n)
        return ans

if __name__ == "__main__":
    n = 3
    sol=Solution()
    ans = sol.generateBinaryStrings(n)
    print(ans)

    