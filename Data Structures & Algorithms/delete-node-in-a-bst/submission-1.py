# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        current = root
        if key > current.val:
            current.right = self.deleteNode(current.right, key)
        elif key < current.val:
            current.left = self.deleteNode(current.left, key)
        elif key == current.val:
            if not current.left:
                return current.right
            elif not current.right:
                return current.left
            else:
                minValue = self.findMinValue(current.right)
                current.val = minValue
                current.right = self.deleteNode(current.right, minValue)
        return root
    def findMinValue(self, root):
        current = root
        while current and current.left:
            current = current.left
        return current.val