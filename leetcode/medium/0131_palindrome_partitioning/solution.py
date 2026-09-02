"""Canonical solution metadata.

Problem Number: 131
Problem Title: Palindrome Partitioning
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: String, Dynamic Programming, Backtracking
Study Tags: Palindrome pruning
Canonical URL: https://leetcode.com/problems/palindrome-partitioning/
"""

"""
Problem:
Word Search (LeetCode 79)

Given an m x n board and a word, return true if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.
"""

#!IDEA
# Use backtracking (DFS).
# 1. Start DFS from every cell that matches the first letter.
# 2. At each step, mark the current cell as visited (in-place by '#').
# 3. Explore 4 neighbors, backtrack by restoring the character.
# 4. If idx == len(word), we found the word.
#
# Optimizations:
# - Early pruning: check if board has enough frequency of each char.
# - Heuristic: reverse the word if last char is rarer than the first.

from typing import List
from collections import Counter

# --- Plain DFS with in-place marking ---
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])

        def find(i, j, idx):
            if idx == len(word):
                return True

            tmp,board[i][j] = board[i][j],'#'
            directions = [(-1,0),(0,1),(1,0),(0,-1)]
            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                if 0 <= nr < n and 0 <= nc < m and board[nr][nc] != '#' and board[nr][nc] == word[idx]:
                    if find(nr, nc, idx+1):
                        return True

            board[i][j] = tmp
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if find(i, j, 1):
                        return True
        return False



# --- Optimized DFS with pruning ---
class SolutionOptimized:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])

        # Early pruning: check if board has enough chars
        board_count = Counter(ch for row in board for ch in row)
        word_count = Counter(word)
        for ch in word_count:
            if word_count[ch] > board_count.get(ch, 0):
                return False

        # Heuristic: reverse if last char rarer than first
        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]

        def dfs(i, j, idx):
            if idx == len(word):
                return True

            if i < 0 or i >= n or j < 0 or j >= m or board[i][j] != word[idx]:
                return False

            tmp, board[i][j] = board[i][j], '#'

            res = (
                dfs(i+1, j, idx+1) or
                dfs(i-1, j, idx+1) or
                dfs(i, j+1, idx+1) or
                dfs(i, j-1, idx+1)
            )

            board[i][j] = tmp
            return res

        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True
        return False


# --- Test Function with ✅ / ❌ ---
def test_solution(func, test_cases):
    for idx, (board, word, expected) in enumerate(test_cases, 1):
        output = func([row[:] for row in board], word)
        if output == expected:
            print(f"Test case {idx}: ✅ True")
        else:
            print(f"Test case {idx}: ❌ Failed")
            print(f"  Board: {board}")
            print(f"  Word: {word}")
            print(f"  Output: {output}")
            print(f"  Expected: {expected}")


# --- Test Cases ---
test_cases = [
    (
        [
            ["A","B","C","E"],
            ["S","F","C","S"],
            ["A","D","E","E"]
        ], 
        "ABCCED", 
        True
    ),
    (
        [
            ["A","B","C","E"],
            ["S","F","C","S"],
            ["A","D","E","E"]
        ], 
        "SEE", 
        True
    ),
    (
        [
            ["A","B","C","E"],
            ["S","F","C","S"],
            ["A","D","E","E"]
        ], 
        "ABCB", 
        False
    ),
    (
        [
            ["A","B","C","E"],
            ["S","F","C","S"],
            ["A","D","E","E"]
        ], 
        "ABFSAB", 
        False
    ),
    (
        [
            ["A","B","C","E"],
            ["S","F","C","S"],
            ["A","D","E","E"]
        ], 
        "ABCD", 
        False
    ),
]


# --- Run Tests ---
if __name__ == "__main__":
    print("Testing SolutionDFS:")
    test_solution(lambda b, w: Solution().exist(b, w), test_cases)

    print("\nTesting SolutionOptimized:")
    test_solution(lambda b, w: SolutionOptimized().exist(b, w), test_cases)
