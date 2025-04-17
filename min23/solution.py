from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeNodeMy:
    def __init__(self, node: TreeNode):
        self.val = node.val
        self.left = TreeNodeMy(node.left) if node.left else None
        self.right = TreeNodeMy(node.right) if node.right else None
        self.checkBalance()
    
    def toOrigin(self):
        return TreeNode(self.balance, 
                        self.left.toOrigin() if self.left else None,
                        self.right.toOrigin() if self.right else None)
    def checkBalance(self):
        left_height = self.left.height if self.left else -1
        right_height = self.right.height if self.right else -1
        self.height = 1 + max(left_height, right_height)
        self.balance = right_height - left_height
    
    def __smallLeft(self, node: TreeNode) -> TreeNode:
        newHead = node.right
        tmp = node.right.left
        node.right.left = node
        node.right = tmp
        node.checkBalance()
        newHead.checkBalance()
        return newHead
    
    def __smallRight(self, node: TreeNode) -> TreeNode:
        newHead = node.left
        tmp = node.left.right
        node.left.right = node
        node.left = tmp
        node.checkBalance()
        newHead.checkBalance()
        return newHead
    
    def fix(self) -> TreeNode: #  returns new head
        if self.balance == 2: # left rotation
            if 0 <= self.right.balance <= 1: # small left
                return self.__smallLeft(self)
            elif self.right.balance == -1: # big left
                self.right = self.__smallRight(self.right)
                return self.__smallLeft(self)
        elif self.balance == -2: # right rotation
            if -1 <= self.left.balance <= 0: # small left
                return self.__smallRight(self)
            elif self.left.balance == 1: # big right
                self.right = self.__smallLeft(self.left)
                return self.__smallRight(self)

        
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        temp = TreeNodeMy(root)

# tree = TreeNode(2, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(5, None, TreeNode(6))))
# tree2 = TreeNodeMy(tree)
# tree2 = tree2.fix()

# tree = TreeNode(3, TreeNode(2), TreeNode(7, TreeNode(5, TreeNode(4), TreeNode(6)), TreeNode(9)))
# tree2 = TreeNodeMy(tree)
# tree2 = tree2.fix()
# print("lol")

tree = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
tree2 = TreeNodeMy(tree)
tree2 = tree2.fix()
print("lol")