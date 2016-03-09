# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    The count-and-say sequence is the sequence of integers beginning as follows:
        1, 11, 21, 1211, 111221, ...
    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.
    Given an integer n, generate the nth sequence.
Note: The sequence of integers will be represented as a string.

Tags: String
Time: O(n^2)
Space: O(n)
从1开始后，后面的数字组成为多个"连续相同字符的出现次数+字符"
'''


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        seq = '1'
        for i in xrange(n-1):
            seq = self.getNext(seq)
        return seq

    def getNext(self, seq):
        i = 0
        next_seq = ''
        while i < len(seq):
            cnt = 1    # 计数器
            while i < len(seq)-1 and seq[i] == seq[i+1]:
                cnt += 1
                i += 1
            next_seq += str(cnt) + seq[i]
            i += 1
        return next_seq


if __name__ == '__main__':
    print Solution().countAndSay(4)
