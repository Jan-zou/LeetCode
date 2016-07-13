# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Design and implement a TwoSum class.
    It should support the following operations: add and find.
    add(input) – Add the number input to an internal data structure.
    find(value) – Find if there exists any pair of numbers which sum is equal to the value.
    For example,
    add(1); add(3); add(5); find(4)􏰀->true; find(7)->􏰀false

Tags: Array
'''

# Store input in hash table
# add – O(1) runtime, find – O(n) runtime, O(n) space
class TwoSum:
    def __init__(self):
        self.nums = []
        self.target = 0

    def add(self, input):
        self.nums.append(input)

    def find(self, value):
        self.target = value
        searchdict = {}
        for i, w in enumerate(self.nums):
            if self.target - w in searchdict:
                return True
            searchdict[w] = i
        return False


# Or Binary search + Two pointers: Maintain a sorted array of numbers.
# add – O(log n) runtime, find – O(n) runtime, O(n) space
