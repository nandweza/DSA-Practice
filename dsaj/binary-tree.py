"""Given a binary tree, return the inorder traversal of it's node's value"""

from typing import List

#defining the binary tree
class Node:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x

#recursive
class Solution():
    def InorderTravrsal(self, root: Node) -> List[int]:
        if root is None:
            return []
        
        return self.InorderTravrsal(root.left) + [root.val] + self.InorderTravrsal(root.right)

#iterative
class Solution2():
    def InorderTraversal(self, root: Node) -> List[int]:
        stack = []
        result = []

        while root is not None or stack != []:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result
