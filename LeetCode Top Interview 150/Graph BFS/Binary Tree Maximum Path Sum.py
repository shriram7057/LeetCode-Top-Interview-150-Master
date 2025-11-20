class Solution(object):
    def maxPathSum(self, root):
        self.maxSum = float('-inf')

        def dfs(node):
            if not node:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            self.maxSum = max(self.maxSum, node.val + left + right)
            return node.val + max(left, right)

        dfs(root)
        return self.maxSum
