# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Description:
    Given an absolute path for a file (Unix-style), simplify it.
    For example,
        path = "/home/", => "/home"
        path = "/a/./b/../../c/", => "/c"
Corner Cases:
    + Did you consider the case where path = "/../"? In this case, you should return "/".
    + Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
      In this case, you should ignore redundant slashes and return "/home/foo".

Tags: Stack, String
'''


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        tokens = path.split('/')
        for token in tokens:
            if token != '..' and token != '.' and token:
                stack.append(token)
            elif token == '..' and stack:
                stack.pop()
        return '/' + '/'.join(stack)


if __name__ == '__main__':
    print Solution().simplifyPath('/../')
    print Solution().simplifyPath('/home//foo/')
    print Solution().simplifyPath('/a/./b/../../c/')
