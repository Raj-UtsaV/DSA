"""Reusable reference: lower and upper bound."""

from bisect import bisect_left,bisect_right
def lower_bound(values,target):return bisect_left(values,target)
def upper_bound(values,target):return bisect_right(values,target)
