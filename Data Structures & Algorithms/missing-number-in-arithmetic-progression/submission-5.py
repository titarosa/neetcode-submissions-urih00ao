class Solution:
    def missingNumber(self, arr: List[int]) -> int:

        diff = min(
            abs(arr[0] - arr[1]),
            abs(arr[-2] - arr[-1])
            )

        for i in range(len(arr) - 1): 
            if arr[i] < arr[i + 1]:
                if abs(arr[i] - arr[i + 1]) != diff:
                    return arr[i] + diff
            elif arr[i] > arr[i + 1]:
                if abs(arr[i] - arr[i + 1]) != diff: 
                    return arr[i + 1] + diff
            elif arr[i] == arr[i + 1]:
                return arr[i]
                



        