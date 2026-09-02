"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Case-insensitive Palindrome
Platform: Other
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Two Pointers, String
Canonical URL: Unresolved
"""

def is_palindrome(text):
 normalized=''.join(ch.lower() for ch in text if ch.isalnum());return normalized==normalized[::-1]
