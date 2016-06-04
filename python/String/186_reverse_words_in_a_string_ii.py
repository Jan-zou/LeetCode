# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given an input string, reverse the string word by word.
    A word is defined as a sequence of non-space characters.
    The input string does not contain leading or trailing spaces and the words are always separated by a single space.
    For example,
        Given s = "the sky is blue",
        return "blue is sky the".
    Could you do it in-place without allocating extra space?

Tags: String

Time: O(n), Space: O(1)
In-place: 整个字符串翻转，然后其中每个词翻转
'''


class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        # in-place
        self.reverse(s, 0, len(s))

        i = 0
        for j in xrange(len(s)+1):
            if j == len(s) or s[j] == ' ':
                self.reverse(s, i, j)
                i = j + 1
        return s

    def reverse(self, s, start, end):
        for i in xrange((end-start)//2):
            s[start+i], s[end-i-1] = s[end-i-1], s[start+i]


if __name__ == '__main__':
    s = ['h','e','l','l','o', ' ', 'w', 'o', 'r', 'l', 'd']
    print Solution().reverseWords(s)


# Challenge 2:
# Rotate an array to the right by k steps in-place without allocating extra space.
# For instance, with k = 3, the array [0, 1, 2, 3, 4, 5, 6] is rotated to [4, 5, 6, 0, 1, 2, 3].
def rotate_k_step(s, k):
    reverse(s, 0, len(s))
    reverse(s, 0, k)
    reverse(s, k, len(s))
    return s

def reverse(s, start, end):
    for i in xrange((end-start)//2):
        s[start+i], s[end-i-1] = s[end-i-1], s[start+i]
