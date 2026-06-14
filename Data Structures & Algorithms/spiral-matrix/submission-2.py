class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        result = []
        l, t = 0, 0
        r = len(matrix[0])-1
        b = len(matrix)-1
        while l <=r and t<=b:
            for j in range(l, r+1):
                result.append(matrix[t][j])
            t+=1

            for i in range(t, b+1):
                result.append(matrix[i][r])
            r-=1
            
            if t>b:
                break

            for j in range(r, l-1, -1):
                result.append(matrix[b][j])
            b-=1

            if l > r:
                break
            
            for i in range(b, t-1, -1):
                result.append(matrix[i][l])
            l+=1
        return result
        

        