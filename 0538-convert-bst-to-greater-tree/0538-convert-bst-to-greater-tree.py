# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    total = 0
    def convertBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        return self.traverseBstTree(root)
        
    def traverseBstTree(self,node):
        print(node)
        if node==None:
            return
        self.traverseBstTree(node.right)
        self.total += node.val
        node.val = self.total
        self.traverseBstTree(node.left)
        return node