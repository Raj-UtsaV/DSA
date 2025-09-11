"""
A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.

A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

"""

#! IDEA
"""

let n - 5 then  _ _ _ _ _
there are 3 even places that can take values form the set {0,2,4,6,8}
and there are 2 odd places that can take the values from the set {2,3,5,7}

? so there are toal pow(5,3)*pow(4,2) possible solutions

TODO: In General
    total possibility = pow(5,even_places)*pow(4,odd_paces)
    even_places = n//2 + n%2
    odd_places = n//2


"""
class Solution:
    mod = 10**9 + 7

    @staticmethod
    def power(self, base, exp):
        if exp == 0:
            return 1
        half = self.power(base, exp // 2)  # integer division
        half = (half * half) % self.mod
        if exp % 2 == 1:
            half = (half * base) % self.mod
        return half

    @staticmethod
    def countGoodNumbers(self, n: int) -> int:
        odd = n // 2
        even = n // 2 + n % 2
        return (self.power(5, even) * self.power(4, odd)) % self.mod


if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    sol = Solution()
    print(sol.countGoodNumbers(n))
