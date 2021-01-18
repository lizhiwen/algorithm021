from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word:str) -> None:
        cur = self.root
        for w in word:
            cur = cur.children[w]
        cur.word = word
        
    
    def search(self,word:str) -> bool:
        cur = self.root        
        for w in word:
            if w not in cur.children:
                return False
            cur = cur.children[w]
        return cur.word

class Solution:
    def __init__(self):
        self.res = []
        self.tree = Trie()
    
    def findWords(self,board,words) -> list([str]):
        def dfs(r,c,root):
            if r<0 or r>(len(board)-1) or c<0 or c>(len(board[0])-1):
                return False
            if board[r][c] not in root.children:
                return False
            if root.children[board[r][c]].word:
                self.res.append(root.children[board[r][c]].word)
                root.children[board[r][c]].word = None
            tmp = board[r][c]
            board[r][c] = '*'
            dfs(r+1,c,root.children[tmp])
            dfs(r-1,c,root.children[tmp])
            dfs(r,c+1,root.children[tmp])
            dfs(r,c-1,root.children[tmp])
            board[r][c] = tmp
        
        for word in words:
            self.tree.insert(word)
            
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r,c,self.tree.root)
        return sorted(self.res)
    
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(Solution().findWords(board,words))