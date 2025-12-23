# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxSumBST(self, root):
        self.max_sum = 0
        
        def dfs(node):
            if not node:
                # isBST, minVal, maxVal, sum
                return True, float('inf'), float('-inf'), 0
            
            left_isBST, left_min, left_max, left_sum = dfs(node.left)
            right_isBST, right_min, right_max, right_sum = dfs(node.right)
            
            # Check if subtree is BST
            if left_isBST and right_isBST and left_max < node.val < right_min:
                curr_sum = left_sum + right_sum + node.val
                self.max_sum = max(self.max_sum, curr_sum)
                
                return (
                    True,
                    min(left_min, node.val),
                    max(right_max, node.val),
                    curr_sum
                )
            
            return False, 0, 0, 0  # Not a BST
        
        dfs(root)
        return self.max_sum

