class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def distributeCandy(self, root):
        self.moves = 0
        def dfs(root):
            if not root:
                return 0
                
            left_requires = dfs(root.left)
            right_requires = dfs(root.right)
            
            self.moves += abs(left_requires) + abs(right_requires)
            remaining_coins = left_requires + right_requires + root.data - 1
            
            return remaining_coins  
        dfs(root)
        return self.moves