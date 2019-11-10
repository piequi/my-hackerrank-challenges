#!/bin/python

from bst import BinarySearchTree
from bst import Node

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''


def height(root):

    height_left = 0
    height_right = 0

    if root.left is None and root.right is None:
        return int(0)

    if root.left:
        height_left = height(root.left)

    if root.right:
        height_right = height(root.right)

    return int((height_left if height_left > height_right else height_right) + 1)


if __name__ == '__main__':
    tree = BinarySearchTree()
    t = int(input())

    arr = list(map(int, input().split()))

    for i in range(t):
        tree.create(arr[i])

    print(height(tree.root))
