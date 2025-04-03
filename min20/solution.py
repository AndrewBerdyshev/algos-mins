class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        if not root: 
            return 'x'
        return str(root.val), self.serialize(root.left), self.serialize(root.right)

    def deserialize(self, data):
        if data[0] == 'x': 
            return None
        node = TreeNode(int(data[0]), self.deserialize(data[1]), self.deserialize(data[2]))
        return node

codec = Codec()
test = [1,2,3,None,None,4,5]
test = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
aboba = codec.serialize(test)
print(aboba)
tree = codec.deserialize(aboba)

print(tree)