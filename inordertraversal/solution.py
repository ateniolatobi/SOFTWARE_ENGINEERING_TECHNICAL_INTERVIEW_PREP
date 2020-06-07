# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __stack(self, root, stack):
        while root:
            stack.append(root)
            root = root.left
            
            
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = []
        out = []
        self.__stack(root, stack)
        while stack:
            node = stack.pop()
            out.append(node.val)
            if node.right:
                root = node.right
                self.__stack(root, stack)
                
        return out
            
                
