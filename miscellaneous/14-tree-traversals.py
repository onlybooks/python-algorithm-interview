class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = Node('F',
            Node('B',
                 Node('A'),
                 Node('D',
                      Node('C'), Node('E'))),
            Node('G',
                 None,
                 Node('I', Node('H'))
                 )
            )


def preorder(node):
    if node is None:
        return
    print(node.val)
    preorder(node.left)
    preorder(node.right)


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)


def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val)


preorder(root)
inorder(root)
postorder(root)
