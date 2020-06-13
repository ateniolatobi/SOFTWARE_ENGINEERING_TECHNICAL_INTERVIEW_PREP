# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return 
        
        out = []
        def helper(node,i):
            if i > len(out):
                out.append(node.val)
            if node.right:
                helper(node.right, i+1)
            if node.left:
                helper(node.left, i+1)
                
        
        helper(root, 1)
        return out
