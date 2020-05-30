# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        def checker(s, t):
            if (not s and t) or (not t and s):
                return False
            if not s and not t:
                return True
            if s.val != t.val:
                return False
            
            return checker(s.left, t.left) and checker(s.right, t.right)
        
        
        def helper(s, t):
            if (not s and t) or (not t and s):
                return False
            if not s and not t:
                return True
            
            if s.val == t.val:
                if checker(s, t):
                    # print('s is {0} and t is {1}'.format(s.val, t.val))
                    return True
            return helper(s.left, t) or helper(s.right, t)
        return helper(s, t)

            

