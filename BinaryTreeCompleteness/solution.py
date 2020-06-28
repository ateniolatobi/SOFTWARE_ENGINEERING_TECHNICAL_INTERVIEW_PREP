# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue = deque()
        queue.append(root)
        isNone = False
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if isNone and node != '#':
                    return False
                elif node == '#':
                    isNone = True
                    continue
                if node.left:
                    queue.append(node.left)
                else:
                    queue.append('#')
                if node.right:
                    queue.append(node.right)
                else:
                    queue.append('#')
        return True