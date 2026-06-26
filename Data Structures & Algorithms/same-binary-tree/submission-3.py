# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if bool(p) != bool(q):
            return False
        if not p:
            return True
        queueA=deque([p])
        queueB=deque([q])
    
        while queueA:
            for i in  range(len(queueA)):
                node1=queueA.popleft()
                node2=queueB.popleft()
                if node1.val!=node2.val:
                    return False
                if bool(node1.left)!=bool(node2.left):
                    return False    
                if node1.left :
                    queueA.append(node1.left)
                    queueB.append(node2.left)
                if bool(node1.right)!=bool(node2.right):
                    return False
                if node1.right :
                    queueA.append(node1.right)
                    queueB.append(node2.right)
        return True
        

        