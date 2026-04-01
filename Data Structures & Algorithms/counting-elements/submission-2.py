class Solution:
    def countElements(self, arr: List[int]) -> int:

        count = 0
        lookup = set(arr)

        for i in range(len(arr)):
            num = arr[i] + 1
            if num in lookup:
                count += 1
        return count
