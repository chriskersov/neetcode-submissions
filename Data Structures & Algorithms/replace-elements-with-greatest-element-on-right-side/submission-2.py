class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # result_arr = []
        # n = len(arr)
        # for i in range(len(arr) - 1):
        #     max_on_right = max(arr[i + 1:n])
        #     result_arr.append(max_on_right)
        # result_arr.append(-1)
        # return result_arr
        max_on_right = -1
        for i in range(len(arr) - 1, -1, -1):
            new_max_on_right = max(arr[i], max_on_right)
            arr[i] = max_on_right
            max_on_right = new_max_on_right
        return arr