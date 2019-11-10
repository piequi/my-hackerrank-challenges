def checkBST(root):

    def checkNode(node, min, max):
        if node is None:
            return True
        else:
            return int(max) > node.data > int(min) \
                   and checkNode(node.left, min, node.data) \
                   and checkNode(node.right, node.data, max)

    return checkNode(root, 0, 100000)
