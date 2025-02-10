def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        que = deque([root])

        while que:

          # go throgth the same level nodes and save the right side node val
            l_que = len(que)
            for i in range(l_que):
                node = que.popleft()
      
                if node and i+1 == l_que: 
                    ans.append(node.val)
                if node:
                    if node.left: que.append(node.left)
                    if node.right: que.append(node.right)

        return ans
  # time: O(N)
  # space: O(N)
