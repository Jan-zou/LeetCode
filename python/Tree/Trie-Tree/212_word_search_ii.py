# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Given a 2D board and a list of words from the dictionary, find all words in the board.
    Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring.
    The same letter cell may not be used more than once in a word.

    For example,
    Given words = ["oath","pea","eat","rain"] and board =
        [
          ['o','a','a','n'],
          ['e','t','a','e'],
          ['i','h','k','r'],
          ['i','f','l','v']
        ]
    Return ["eat","oath"].

Note:
    You may assume that all inputs are consist of lowercase letters a-z.
    You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?
    If the current candidate does not exist in all words' prefix, you could stop backtracking immediately.
    What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie?
    If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.

Tags: Backtracking, Trie
'''


class TrieNode:
    def __init__(self):
        self.is_string = False
        self.leaves = {}

    def insert(self, word):
        current = self
        for c in word:
            if c not in current.leaves:
                current.leaves[c] = TrieNode()
            current = current.leaves[c]
        current.is_string = True


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        visited = [[False for j in xrange(len(board[0]))] for i in xrange(len(board))]
        result = {}
        trie = TrieNode()
        for word in words:
            trie.insert(word)

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.findWordsRecu(board, trie, 0, i, j, visited, [], result):
                    return True
        return result.keys()


    def findWordsRecu(self, board, trie, current, i, j, visited, current_str, result):
        if not trie or i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j]:
            return

        if board[i][j] not in trie.leaves:
            return

        current_str.append(board[i][j])
        next_node = trie.leaves[board[i][j]]
        if next_node.is_string:
            result[''.join(current_str)] = True

        visited[i][j] = True
        self.findWordsRecu(board, next_node, current + 1, i + 1, j, visited, current_str, result)
        self.findWordsRecu(board, next_node, current + 1, i - 1, j, visited, current_str, result)
        self.findWordsRecu(board, next_node, current + 1, i, j + 1, visited, current_str, result)
        self.findWordsRecu(board, next_node, current + 1, i, j - 1, visited, current_str, result)
        visited[i][j] = False
        current_str.pop()


if __name__ == '__main__':
    words = ["oath","pea","eat","rain"]
    board =[['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']]
    print Solution().findWords(board, words)
