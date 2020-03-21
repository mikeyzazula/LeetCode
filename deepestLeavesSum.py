# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q1 = []
        q1.append(root)
        q2 = [] # going to be our queue we use for the next level
        
        treeDict = {} # this will contain lists of every node at each level, we can index to the end and sum
        level = 0
        while q1:
            current = q1.pop()
            
            if level not in treeDict:
                treeDict[level] = current.val
            else:
                treeDict[level] += current.val
            
            if current.left:
                q2.append(current.left)
            if current.right:
                q2.append(current.right)
                
            if not q1:
                q1 = q2
                q2 = []
                level += 1
        
        return treeDict[max(treeDict, key=int)]
            
