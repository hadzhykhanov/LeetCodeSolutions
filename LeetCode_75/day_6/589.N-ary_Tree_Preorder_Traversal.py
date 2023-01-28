from queue import Queue

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        """1. iterative using stack"""
        if not root:
            return []

        ans = []
        stack = [root]
        while stack:
            curr = stack.pop()
            ans.append(curr.val)
            stack.extend(reversed(curr.children))
        return ans


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        """recursive"""
        if not root:
            return []

        ans = []

        def preorder_traversal(root):
            ans.append(root.val)
            for node in root.children:
                preorder_traversal(node)

        preorder_traversal(root)
        return ans

