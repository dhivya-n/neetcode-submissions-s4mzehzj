class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if curr.children[index] == 0:
                curr.children[index] = Node()
            curr = curr.children[index]
        curr.word = True
        
    def searchNode(self, word: str, curr, letterIndex) -> bool:
        if letterIndex == len(word):
            return curr.word
        if word[letterIndex] == '.':
            res = False
            for i in range(26):
                if curr.children[i] != 0:
                    res = res or self.searchNode(word, curr.children[i], letterIndex+1)
                    if res:
                        return True
            return res

        else:
            letter = ord(word[letterIndex]) - ord('a') 
            if curr.children[letter] == 0:
                return False
            else:
                return self.searchNode(word, curr.children[letter], letterIndex+1)
    def search(self, word: str) -> bool:
        return self.searchNode(word, self.root, 0)

        
class Node:
    def __init__(self):
        self.children = [0]*26
        self.word = False