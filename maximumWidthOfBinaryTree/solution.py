# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        
        g = {}
        #
        def helper(node, level, column):
            if not node:
                return
            
            if level in g:
                g[level].append(column)
            else:
                g[level] = [column]
            
            helper(node.left, level+1, column*2)
            helper(node.right, level+1, column*2 + 1)
            
        helper(root, 0, 0)
        out = 0
        for key in g:
            level = g[key]
            if len(level) == 1:
                out = max(out, 1)
            else:
                low, high = level[0], level[-1]
                out = max(out, high - low + 1)
        return out