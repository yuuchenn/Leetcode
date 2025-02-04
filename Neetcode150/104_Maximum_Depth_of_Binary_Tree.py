# 1. recursive
def maxDepth(self, root: Optional[TreeNode]) -> int:
  if not root:
    return 0
  return  1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
# time :O(N)
# space:O(N)

# 2.BFS - queue
def maxDepth(self, root: Optional[TreeNode]) -> int:
  if not root:
    return 0
    
  queue = deque([root])
  depths = 0
  while queue:
    for i in range(len(queue)):
      node = queue.popleft()
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
    depths += 1
    
  return depths
# time :O(N)
# space:O(N)

# 3. DFS - stack
def maxDepth(self, root: Optional[TreeNode]) -> int:
  if not root:
    return 0

  stack = [[root, 1]]
  depths = 0
  while stack:
    node, dep = stack.pop()
    if node : 
      depths = max(depths,dep)
      stack.append([node.left, dep+1])
      stack.append([node.right, dep+1])
    
  return depths
  
# time :O(N)
# space:O(N)
