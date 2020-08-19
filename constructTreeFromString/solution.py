# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        
        
        
        out = []
        def helper(t):
            if not t:
                return 
                
            out.append(str(t.val))
            if t.left or t.right:
                out.append('(')
                helper(t.left)
                out.append(')')
            if t.right:
                out.append('(')
                helper(t.right)
                out.append(')')
            
        helper(t)
        return ''.join(out)
            