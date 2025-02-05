def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = 0
        # return height of the node
        def height(root):
            if not root:
                return 0

            left = height(root.left)
            right = height(root.right)
            self.ans = max(self.ans, abs(left - right))

            return 1 + max(left,right)
        
        height(root)
        return True if self.ans <= 1 else False 
    
# time : O(N^2)
# sapce : O(N)

def isBalanced(self, root: Optional[TreeNode]) -> bool:
  
        # return height of the node
        def height(root):
            if not root:
                return 0

            left = height(root.left)
            right = height(root.right)
          
          #  stop recursive if find the unbalance node
            if left == -1 or right == -1 or abs(left-right) > 1:
              return -1

            return 1 + max(left,right)
        
        return height(root) != -1

# time : O(N)
# sapce : O(N)
