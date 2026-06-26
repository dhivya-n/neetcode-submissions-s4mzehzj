from typing import List

class Solution:
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.constructTrie(words)
        self.result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.searchTrie(board, i, j, self.root, '')
        return list(self.result)

        
    def searchTrie(self, board, i, j, node, prefix):
        if i < 0 or j < 0 or i == len(board) or j == len(board[0]):
            return 
        
        word = prefix + board[i][j]
        curr = board[i][j]
        if board[i][j] not in node.children:
            return


        if node.children[board[i][j]].is_word:
            self.result.add(word)
            node.refs -= 1
        board[i][j] = '#'
        self.searchTrie(board, i+1, j, node.children[curr], word)
        self.searchTrie(board, i, j+1, node.children[curr], word)
        self.searchTrie(board, i-1, j, node.children[curr], word)
        self.searchTrie(board, i, j-1, node.children[curr], word)
        board[i][j] = curr
        if node.refs == 0:
            del node.children[board[i][j]] 
            return

    def constructTrie(self, words):
        self.root = TrieNode()
        self.root.refs +=1
        for word in words:
            curr = self.root
            for letter in word:
                if letter not in curr.children:
                    curr.children[letter] = TrieNode()
                curr = curr.children[letter]
                curr.refs += 1
            curr.is_word = True
        return

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.refs = 0
