# Usually level order traversal lets us scan a level of tree which helps in 
# problems like Right/Left View and just normal level stuff, yay

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# root = [1,2,3,4,5,None,8,None,None,6,7,9]       Creating this as a tree
root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = None
root.right.right = TreeNode(8)

root.left.left.left = None
root.left.left.right = None

root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(7)

root.right.right.left = TreeNode(9)
root.right.right.right = None

class Solution:
    def LevelOrder(self, root:TreeNode):
        if root == None: return []
        ans = []

        q = deque()
        q.append(root)

        while q:
            curr = []
            for i in range(len(q)):
                node = q.popleft()
                curr.append(node.val)               # For current level

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(curr.copy())
        
        return ans

ans = Solution.LevelOrder(Solution, root)
print(ans)