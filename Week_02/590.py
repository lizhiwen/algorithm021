class Solution:
    def postorder(self, root) :
        result = []

        def postHelper(root):
            if not root:
                return None
            children = root.children
            for child in children:
                postHelper(child)
            result.append(root.val)

        postHelper(root)
        return result