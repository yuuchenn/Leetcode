def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        que = deque([root]) # save same level nodes
        # queue 
        while que:
            temp = []
            for i in range(len(que)):
                node = que.popleft()
                if node:
                    temp.append(node.val)
                    que.append(node.left)
                    que.append(node.right)
            
            if temp:
                ans.append(temp)
        return ans

# time: O(N)
# space:O(N)
