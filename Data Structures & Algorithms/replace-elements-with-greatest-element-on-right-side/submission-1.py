class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result_arr = []
        for i in range(len(arr) - 1):
            max_on_right = arr[i + 1]
            for j in range(i + 1, len(arr)):
                max_on_right = max(max_on_right, arr[j])
            result_arr.append(max_on_right)
        result_arr.append(-1)
        return result_arr
