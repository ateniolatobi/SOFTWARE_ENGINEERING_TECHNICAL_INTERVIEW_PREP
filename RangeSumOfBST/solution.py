# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        
        
        
        # out = 0
        
        def helper(root):
            # nonlocal out
            if not root:
                return 0
            out = 0
            if L<=root.val<=R:
                out = root.val
            #     retur
            if root.val >= L:
                out += helper(root.left)
                
            if root.val <= R:
                out += helper(root.right)            
            return out
            
            
        return helper(root)
        