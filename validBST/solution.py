# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __isValidBST(self, root, leftBound, rightBound):
        
        if not leftBound < root.val < rightBound:
            return False
        
        if not root.left and not root.right:
            return True
        if root.left:
            left = self.__isValidBST(root.left, leftBound, root.val)
            if not left:
                return False
        if root.right:
            right = self.__isValidBST(root.right, root.val, rightBound)
            if not right:
                return False
        
        return True
    
    
    
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.__isValidBST(root, float('-inf'), float('inf'))
