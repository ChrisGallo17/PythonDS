class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.length = 0       # modified directly by dfs()
        if root:
            self.dfs(root)
        return self.length

    def dfs(self, root: TreeNode) -> int:
        # Recursive postorder traversal
        left = self.dfs(root.left) if root.left else 0
        right = self.dfs(root.right) if root.right else 0
        # Record the longest path seen so far
        self.length = max(self.length, left + right)
        # Return the longest path through this subtree root
        return max(left, right) + 1
