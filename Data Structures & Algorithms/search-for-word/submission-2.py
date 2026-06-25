class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        lookup = {}
        res = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                   res = self.search(board, word, i, j, 0)
                   if res:
                    return True
        return False
    
    def search(self, board, word, bi, bj, wi, seen = None):
        if wi == len(word):
            return True
        
        #out of bounds
        if bi < 0 or bj < 0 or bi == len(board) or bj == len(board[0]):
            return False
        seen = set() if seen is None else seen
        if (bi, bj) in seen:
            return False

        if board[bi][bj] != word[wi]:
            return False

        seen.add((bi, bj))
        res = self.search(board, word, bi-1, bj, wi+1, seen) or self.search(board, word, bi, bj-1, wi+1, seen) or self.search(board, word, bi, bj+1, wi+1, seen) or self.search(board, word, bi+1, bj, wi+1, seen)
        seen.remove((bi, bj))
        return res
        