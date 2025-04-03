from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        projection = []
        if not root:
            return []
        def req(root: TreeNode, i=0):
            if not root:
                return
            if len(projection) == i:
                projection.append(root.val)
            else:
                projection[i] = root.val
            req(root.left, i+1)
            req(root.right, i+1)
        req(root)
        return projection
