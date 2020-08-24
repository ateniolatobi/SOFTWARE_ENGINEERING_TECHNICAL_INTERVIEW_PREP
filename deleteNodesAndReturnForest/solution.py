# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        
        todelete = set(to_delete)
        
        out = []
        def helper(root):
            
            if not root:
                return 
            
            left = helper(root.left)
            if not left:
                root.left = None
            right = helper(root.right)
            if not right:
                root.right = None
            
            
            if root.val in todelete:
                if left:
                    out.append(left)
                if right:
                    out.append(right)
                return None
            else:
                return root
            
        if helper(root):
            out.append(root)
        
        
        
        return out