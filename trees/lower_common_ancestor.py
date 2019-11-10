#!/bin/python

from bst import BinarySearchTree
from bst import Node


def lca(root, v1, v2):

    if root.info > v1 and root.info > v2:
        return lca(root.left, v1, v2)
    elif root.info < v1 and root.info < v2:
        return lca(root.right, v1, v2)
    else:
        return root


if __name__ == '__main__':
    tree = BinarySearchTree()
    t = int(input())

    arr = list(map(int, input().split()))

    for i in range(t):
        tree.create(arr[i])

    v = list(map(int, input().split()))

    ans = lca(tree.root, v[0], v[1])
    print (ans.info)
