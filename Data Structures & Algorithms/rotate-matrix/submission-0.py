class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        n = len(m)
        for j in range(0, math.floor(n/2)):
            for i in range(j, n-1-j):
                top = i
                right = n -1 - j
                left = n - 1 - i 
                bottom = j

                prev = m[bottom][top]

                current = m[top][right]
                m[top][right] = prev
                prev = current

                current = m[right][left]
                m[right][left] = prev
                prev = current

                current = m[left][bottom]
                m[left][bottom] = prev
                prev = current

                m[bottom][top] = prev

