"""
Problem Description:
--------------------
LeetCode 43. Multiply Strings
Link: https://leetcode.com/problems/multiply-strings/

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integers directly.

Example:
--------
Input: num1 = "123", num2 = "456"
Output: "56088"

"""

#!IDEA
"""
The approach mimics grade-school multiplication.
- Reverse both number strings to process digits from least significant to most significant.
- Iterate through each digit of `num2`. For each digit, multiply it with `num1` to get a temporary product string (`temp`).
- This `temp` product is shifted to the left based on the position of the digit in `num2`.
- A helper function `addstring` is used to add this `temp` product to the cumulative `ans` string.
- After iterating through all digits of `num2`, the `ans` string (which is built in reverse) is reversed one last time to get the final result.
"""

class Solution:
    def addstring(self,ans,temp,shift):
        carry = 0
        i = shift
        j = 0
        res = list(ans) if ans else []
        
        while len(res) < i:
            res.append("0")
        
        while j < len(temp) or carry:
            a = int(res[i]) if i < len(res) else 0
            b = int(temp[j]) if j < len(temp) else 0
            s = a + b + carry
            if i < len(res):
                res[i] = str(s % 10)
            else:
                res.append(str(s % 10))
            carry = s // 10
            i += 1
            j += 1
        
        return "".join(res)
        


    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        ans = ""
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(len(num2)):
            temp = ""
            carry = 0
            for j in range(len(num1)):
                mul = int(num1[j]) * int(num2[i]) + carry
                temp += str(mul % 10)
                carry = mul // 10
            
            if carry > 0:
                temp += str(carry)
            
            ans = self.addstring(ans,temp,i)
            
        return ans[::-1]

# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (input_val, expected) in enumerate(test_cases, 1):
        # The function expects two arguments, so we unpack the input tuple
        output = func(*input_val)
        if output == expected:
            print(f"Test case {idx}: ✅ Passed")
        else:
            print(f"Test case {idx}: ❌ Failed")
            print(f"  Input: {input_val}")
            print(f"  Output: {output}")
            print(f"  Expected: {expected}")


# --- Example Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        (("123", "456"), "56088"),
        (("2", "3"), "6"),
        (("999", "0"), "0"),
        (("0", "12345"), "0"),
        (("999", "1"), "999"),
        (("9133", "0"), "0"),
    ]
    
    test_solution(sol.multiply, test_cases)
