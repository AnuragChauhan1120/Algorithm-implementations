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

# PreOrder Traversal (root, left, right)
class Solution1:
    def PreOrderTraversal(self, root:TreeNode):
        if root == None: return []
        ans = []

        def dfs(root):
            if root == None: return

            ans.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ans

# InOrder Traversal (left, root, right)
class Solution2:
    def InOrderTraversal(self, root:TreeNode):
        if root == None: return []
        ans = []

        def dfs(root):
            if root == None: return

            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)

        dfs(root)
        return ans

# PostOrder Traversal (left, right, root)
class Solution3:
    def PostOrderTraversal(self, root:TreeNode):
        if root == None: return []
        ans = []

        def dfs(root):
            if root == None: return

            dfs(root.left)
            dfs(root.right)
            ans.append(root.val)

        dfs(root)
        return ans

preorder = Solution1.PreOrderTraversal(Solution1,root)

inorder = Solution2.InOrderTraversal(Solution2,root)

postorder = Solution3.PostOrderTraversal(Solution3,root)

print(preorder)
print(inorder)
print(postorder)