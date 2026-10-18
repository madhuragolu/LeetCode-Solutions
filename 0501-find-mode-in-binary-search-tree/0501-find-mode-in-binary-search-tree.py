# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        if not root:
            return None
        freq={}
        def mode(root):
            if not root:
                return 
            freq[root.val]=freq.get(root.val,0)+1
            mode(root.left)
            mode(root.right)
        mode(root)
        if not freq:
            return []
        ma=max(freq.values())
        ans=[]
        for k,f in freq.items():
            if f == ma:
                ans.append(k)
        return ans

