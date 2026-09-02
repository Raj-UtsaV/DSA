"""Canonical solution metadata.

Problem Number: 71
Problem Title: Simplify Path
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: String, Stack
Study Tags: Tokenization
Canonical URL: https://leetcode.com/problems/simplify-path/
"""

"""
Problem Description:
--------------------
LeetCode 71. Simplify Path
Link: https://leetcode.com/problems/simplify-path/

Given a string path, which is an absolute path (starting with a '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:
- The path starts with a single slash '/'.
- Any two directories are separated by a single slash '/'.
- The path does not end with a trailing '/'.
- The path contains only the directories on the path from the root directory to the target directory (i.e., no '.' or '..').

Example:
--------
Input: path = "/home//foo/"
Output: "/home/foo"

Input: path = "/a/./b/../../c/"
Output: "/c"

"""

#!IDEA
"""
The problem asks us to simplify a Unix-style absolute path. This can be effectively solved using a stack. The core idea is to process the components of the path, which are the directory/file names separated by slashes.

1.  **Split the Path**: The first step is to split the input `path` string by the '/' delimiter. This will give us a list of all the components between the slashes. For example, "/home//foo/" becomes `['', 'home', '', 'foo', '']`.

2.  **Process Components with a Stack**: We iterate through each component and use a stack to build the sequence of directories in the canonical path.
    - If the component is an empty string `""` or a single dot `"."`, it represents the current directory or a redundant slash, so we do nothing and ignore it.
    - If the component is a double dot `".."`: This means we need to go up one level in the directory hierarchy. We simulate this by popping an element from our stack, but only if the stack is not empty (as we can't go up from the root directory).
    - If the component is anything else (e.g., "home", "foo"): It's a valid directory name. We push it onto the stack.

3.  **Construct the Final Path**: After processing all components, the stack contains the sequence of directories for the simplified path. We join the elements of the stack with a single slash '/' in between.

4.  **Format the Output**: Finally, we prepend a single slash '/' to the joined string to form the absolute canonical path. For example, if the stack is `['home', 'foo']`, joining gives "home/foo", and prepending '/' gives "/home/foo". If the stack is empty, this results in just "/".
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split("/")
        stack = []

        for part in parts:
            if part == "" or part == ".":
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return "/" + "/".join(stack)


    def simplifyPath1(self, path: str) -> str:
        stack = []
        i = 0
        n = len(path)

        while i < n:
            # skip multiple slashes
            while i < n and path[i] == "/":
                i += 1

            substr = ""
            while i < n and path[i] != "/":
                substr += path[i]
                i += 1

            if substr == "" or substr == ".":
                # ignore empty or "."
                continue
            elif substr == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(substr)

        return "/" + "/".join(stack)


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
        ("/home/", "/home"),
        ("/../", "/"),
        ("/home//foo/", "/home/foo"),
        ("/a/./b/../../c/", "/c"),
        ("/a/../../b/../c//.//", "/c"),
        ("/a//b////c/d//././/..", "/a/b/c"),
    ]

    test_solution(sol.simplifyPath, test_cases)
    print("\n")
    test_solution(sol.simplifyPath1, test_cases)
