"""
Problem Description:
--------------------
[problem:] LeetCode 1048. Longest String Chain
[link:] https://leetcode.com/problems/longest-string-chain/
[description:] You are given an array of `words` where each word consists of lowercase English letters. A word `wordA` is a predecessor of `wordB` if and only if we can insert exactly one letter anywhere in `wordA` without changing the order of the other characters to make it equal to `wordB`. For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad". A word chain is a sequence of words `[word1, word2, ..., wordk]` with `k >= 1`, where `word1` is a predecessor of `word2`, `word2` is a predecessor of `word3`, and so on. A single word is a trivial word chain with `k = 1`. Return the length of the longest possible word chain with words chosen from the given list of `words`.

Example:
--------
Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a", "ba", "bda", "bdca"].

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can form a chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].

"""

#!IDEA
"""
This problem asks for the longest sequence of words where each word is a predecessor of the next. This structure is very similar to the Longest Increasing Subsequence (LIS) problem, and we can adapt the LIS dynamic programming approach to solve it.

--- Solution: Dynamic Programming (LIS-based) ---

* Core Idea:
    1.  **Sort the array**: First, sort the input array `words` based on the length of the words. This is a crucial step. If we process words in increasing order of their length, we can be sure that any predecessor of a word `words[i]` must appear before it in the sorted array. This simplifies our search.
    2.  **Apply LIS logic**: After sorting, the problem becomes finding the longest chain where each word is a predecessor of the next.

* State:
    - `dp[i]`: The length of the longest string chain that *ends* with the word `words[i]`.

* Core Logic:
    - Initialize a `dp` array of size `n` with all 1s (each word is a chain of length 1 by itself).
    - Iterate through the sorted `words` array from `i = 0` to `n-1`.
    - For each `i`, iterate through all previous words `j` (from `0` to `i-1`).
    - Check if `words[j]` is a predecessor of `words[i]` using a helper function.
    - If it is, it means we can extend the chain ending at `j`. If this creates a longer chain for `i` (i.e., `1 + dp[j] > dp[i]`), we update `dp[i] = 1 + dp[j]`.

* Predecessor Check (`compare` function):
    - To check if `word1` is a predecessor of `word2`:
        1.  First, `len(word2)` must be exactly `len(word1) + 1`.
        2.  Use two pointers, `i` for `word2` and `j` for `word1`.
        3.  Iterate through both words. If characters match (`word2[i] == word1[j]`), advance both pointers.
        4.  If they don't match, it must be the single inserted character in `word2`, so we only advance the pointer `i`.
        5.  After iterating, if we have successfully traversed all of `word1` (i.e., `j == len(word1)`), then `word1` is a predecessor.

* Result:
    - The length of the longest chain is the maximum value in the `dp` array, as the chain can end with any word.

* Complexity:
    - Time complexity: O(N^2 * L), where N is the number of words and L is the maximum length of a word. Sorting takes O(N log N). The nested loops are O(N^2), and inside them, the `compare` function takes O(L).
    - Space complexity: O(N) for the `dp` array.
"""

from typing import List

class Solution:
    def compare(self, s1: str, s2: str) -> bool:
        """Checks if s1 is a predecessor of s2."""
        if len(s1) + 1 != len(s2):
            return False
        
        first = 0  # pointer for s2
        second = 0 # pointer for s1

        while first < len(s2):
            if second < len(s1) and s1[second] == s2[first]:
                second += 1
            first += 1
        
        return first == len(s2) and second == len(s1)

    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        if n <= 1:
            return n

        # Sort words by their length
        words.sort(key=len)

        dp = [1]*n
        max_chain = 1

        for i in range(n):
            for prev_index in range(i):
                # Check if words[prev_index] is a predecessor of words[i]
                if self.compare(words[prev_index], words[i]) and 1 + dp[prev_index] > dp[i]:
                    dp[i] = 1 + dp[prev_index]
            
            max_chain = max(max_chain, dp[i])

        return max_chain

# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (input_val, expected) in enumerate(test_cases, 1):
        output = func(input_val)
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
        (["a", "b", "ba", "bca", "bda", "bdca"], 4),
        (["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"], 5),
        (["abcd", "dbqca"], 1),
        (["a", "b"], 1),
        (["a"], 1),
        ([], 0)
    ]
    
    test_solution(sol.longestStrChain, test_cases)

"""
Dry Run Example:
---------------
Input: words = ["a", "b", "ba", "bca", "bda", "bdca"]

1. Sort by length:
   words = ["a", "b", "ba", "bca", "bda", "bdca"] (already sorted by length)
   n = 6

2. Initialize:
   dp = [1, 1, 1, 1, 1, 1]
   max_chain = 1

3. DP Calculation:
   i = 0 (word="a"): dp=[1,1,1,1,1,1], max_chain=1
   i = 1 (word="b"): dp=[1,1,1,1,1,1], max_chain=1

   i = 2 (word="ba"):
     prev_index = 0 (word="a"): compare("a", "ba") -> True. 1+dp[0] > dp[2] (2>1). dp[2]=2.
     prev_index = 1 (word="b"): compare("b", "ba") -> True. 1+dp[1] > dp[2] (2>2) -> False.
     dp=[1,1,2,1,1,1], max_chain=2

   i = 3 (word="bca"):
     prev_index = 2 (word="ba"): compare("ba", "bca") -> True. 1+dp[2] > dp[3] (3>1). dp[3]=3.
     dp=[1,1,2,3,1,1], max_chain=3

   i = 4 (word="bda"):
     prev_index = 2 (word="ba"): compare("ba", "bda") -> True. 1+dp[2] > dp[4] (3>1). dp[4]=3.
     dp=[1,1,2,3,3,1], max_chain=3

   i = 5 (word="bdca"):
     prev_index = 3 (word="bca"): compare("bca", "bdca") -> False.
     prev_index = 4 (word="bda"): compare("bda", "bdca") -> True. 1+dp[4] > dp[5] (4>1). dp[5]=4.
     dp=[1,1,2,3,3,4], max_chain=4

Final dp = [1, 1, 2, 3, 3, 4]
Final max_chain = 4

✅ Return: 4
"""