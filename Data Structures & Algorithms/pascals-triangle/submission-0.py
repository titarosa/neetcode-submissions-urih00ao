class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return [ ]
        
        res = [[1]]

        for i in range(1, numRows): 
            prev_row = res[-1]
            new_row = [1]
            for j in range(len(prev_row)-1):
                middle = prev_row[j] + prev_row[j+1]
                new_row.append(middle)
            new_row.append(1)
            res.append(new_row)
        return res




        