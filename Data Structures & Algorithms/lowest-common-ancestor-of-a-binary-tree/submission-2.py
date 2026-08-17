# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        queuee= deque([root])
        parent= {root: None}
        while queuee:
            node=queuee.popleft()
            if node.left:
                queuee.append(node.left)
                parent[node.left]=node
            if node.right:
                queuee.append(node.right)
                parent[node.right]=node
            if p in parent and q in parent:
                break
        ans=set()
        while p:
            ans.add(p)
            p=parent[p]
        while q:
            if q in ans:
                return q
            q=parent[q]
        