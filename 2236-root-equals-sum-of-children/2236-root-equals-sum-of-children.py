# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def checkTree(self, root: TreeNode | None) -> bool:
        q=deque([root])
        if not root:
            return True
        while q:
            cur=q.popleft()
            if not cur.left and not cur.right:
                continue
            left_val=cur.left.val if cur.left else 0
            right_val=cur.right.val if cur.right else 0

            if cur.val!=left_val+right_val:
                return False
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return True
                