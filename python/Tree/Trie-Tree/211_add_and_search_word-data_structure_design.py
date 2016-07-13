# !/usr/bin/env python
# coding: utf-8

'''
Description:
    Design a data structure that supports the following two operations:
        void addWord(word)
        bool search(word)

    search(word) can search a literal word or a regular expression string containing only letters a-z or ..
    A . means it can represent any one letter.

    For example:
        addWord("bad")
        addWord("dad")
        addWord("mad")
        search("pad") -> false
        search("bad") -> true
        search(".ad") -> true
        search("b..") -> true
Note:
    You may assume that all words are consist of lowercase letters a-z.
    You should be familiar with how a Trie works.
    If not, please work on this problem: Implement Trie (Prefix Tree) first.


Tags: Backtracking, Trie, Design
'''


class TrieNode:
    def __init__(self):
        self.is_string = False
        self.leaves = {}

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        current = self.root
        for c in word:
            if c not in current.leaves:
                current.leaves[c] = TrieNode()
            current = current.leaves[c]
        current.is_string = True


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.searchHelper(word, 0, self.root)

    def searchHelper(self, word, start, current):
        if start == len(word):
            return current.is_string

        if word[start] in current.leaves:
            return self.searchHelper(word, start+1, current.leaves[word[start]])
        elif word[start] == '.':
            for c in current.leaves:
                if self.searchHelper(word, start+1, current.leaves[c]):
                    return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
