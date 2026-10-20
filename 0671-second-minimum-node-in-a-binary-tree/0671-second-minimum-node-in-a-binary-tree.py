# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode | None) -> int:
        mi=root.val
        semin=float("inf")
        def minimum(root):
            nonlocal mi
            if not root :
                return mi
            mi=min(mi,root.val)
            minimum(root.left)
            minimum(root.right)
        def seminimum(root):
            nonlocal semin
            if not root:
                return semin
            if mi<root.val<semin:
                semin=min(semin,root.val)
            seminimum(root.left)
            seminimum(root.right)
        minimum(root)
        seminimum(root)
        if semin!=float('inf'):
            return semin
        else:
            return -1
