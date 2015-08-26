class TreeNode(object):

    def __init__(self, payload, left=None, right=None):
        self.left = left
        self.right = right
        self.payload = payload

    def insert(self, item):
        if self.payload == item:
            return
        else:
            if item < self.payload:
                if self.left is not None:
                    self.left.insert(item)
                else:
                    self.left = TreeNode(item)
            else:
                if self.right is not None:
                    self.right.insert(item)
                else:
                    self.right = TreeNode(item)

    def preorder(self):
        print(self.payload)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self, tree):
        if tree is not None:
            self.postorder(tree.left)
            self.postorder(tree.right)
            print(tree.payload)

    def inorder(self, tree):
        if tree is not None:
            self.inorder(tree.left)
            print(tree.payload)
            self.inorder(tree.right)


class BinaryTree(TreeNode):

    def __init__(self, data):
        TreeNode.__init__(self, data)


tree = BinaryTree(10)
tree.insert(12)
tree.insert(9)

tree.preorder()
tree.postorder(tree)
tree.inorder(tree)
