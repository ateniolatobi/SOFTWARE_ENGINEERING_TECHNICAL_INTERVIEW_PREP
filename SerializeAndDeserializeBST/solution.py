# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None






class Codec:
    
    def insert(self, node, val):
        if val < node.val:
            if not node.left:
                node.left = TreeNode(val)
                return
            self.insert(node.left, val)
        elif val > node.val:
            if not node.right:
                node.right = TreeNode(val)
                return
            self.insert(node.right, val)
            
    def serial(self, root, basket):
        
        basket.append(root.val)
        if root.left:
            basket = self.serial(root.left, basket)
        if root.right:
            basket = self.serial(root.right, basket)
        return basket
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return []
        
        temp = self.serial(root, [])
        # print('temp is ', temp)
        return temp
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        # print('chee')
        
        if not data:
            return None
        # print(data)
        root = TreeNode(data[0])
        n = len(data)
        for i in range(1, n):
            v = data[i]
            self.insert(root, v)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))