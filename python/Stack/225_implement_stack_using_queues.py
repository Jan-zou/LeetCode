# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Implement the following operations of a stack using queues.

    + push(x) -- Push element x onto stack.
    + pop() -- Removes the element on top of the stack.
    + top() -- Get the top element.
    + empty() -- Return whether the stack is empty.
Notes:
    + You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
    + Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
    + You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

Tags: Stack, Design
'''

import collections
class Queue:
    def __init__(self):
        self.data = collections.deque()

    def push(self, x):
        self.data.append(x)

    def peek(self):
        return self.data[0]

    def pop(self):
        return self.data.popleft()

    def size(self):
        return len(self.data)

    def empty(self):
        return len(self.data) == 0

# stack top is left
# Time: push: O(n), pop: O(1), top: O(1)
# Space: O(n)
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q_ = Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q_.push(x)
        for _ in xrange(self.q_.size() - 1):
            self.q_.push(self.q_.pop())

    def pop(self):
        """
        :rtype: nothing
        """
        self.q_.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.q_.peek()

    def empty(self):
        """
        :rtype: bool
        """
        return self.q_.empty()

# stack top is right
# Time: push: O(1), pop: O(n), top: O(1)
# Space: O(n)
class Stack2(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q_ = Queue()
        self.top_ = None

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q_.push(x)
        self.top_ = x

    def pop(self):
        """
        :rtype: nothing
        """
        for _ in xrange(self.q_.size() - 1):
            self.top_ = self.q_.pop()
            self.q_.push(self.top_)
        self.q_.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.top_

    def empty(self):
        """
        :rtype: bool
        """
        return self.q_.empty()
