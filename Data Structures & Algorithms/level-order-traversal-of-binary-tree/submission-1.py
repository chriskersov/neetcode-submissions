# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        queue = deque()
        if root:
            queue.append(root)
        level = 0
        result = []
        while len(queue) > 0:
            print(result)
            temp = []
            for i in range(len(queue)):
                current = queue.popleft()
                temp.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            result.append(temp)
        return result