
class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        n = len(m)
        for j in range(0, math.floor(n/2)):
            for i in range(j, n-1-j):
                top = i
                right = n -1 - j
                bottom = n - 1 - i 
                left = j
                prev = m[left][top]

                m[left][top] = m[bottom][left]
                m[bottom][left] = m[right][bottom]
                m[right][bottom] = m[top][right]
                m[top][right] = prev       