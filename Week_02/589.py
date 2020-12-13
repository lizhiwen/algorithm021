class Solution:
    def preorder(self):
        if not root:
            return []
        
        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)

            for child in reversed(node.children):
                stack.append(child)
        return result