def inorderTraversal(self, root):
    def dfs(cur):
        if not cur:
            return      
        # 前序递归
        res.append(cur.val)
        dfs(cur.left)
        dfs(cur.right) 
