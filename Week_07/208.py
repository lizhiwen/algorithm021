from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word:str) -> None:
        cur = self.root
        for w in word:
            cur = cur.children[w]
        cur.is_word = True
        
    
    def search(self,word:str) -> bool:
        cur = self.root        
        for w in word:
            print(cur.children.keys())
            if w not in cur.children:
                return False
            cur = cur.children[w]
        return cur.is_word
    
    def startWith(self,prefix:str) -> bool:
        cur = self.root
        for w in prefix:
            if w not in cur.children:
                return False
            cur = cur.children[w]
        return True
    
Trie = Trie()
Trie.insert("apple")
Trie.insert("app")
print(Trie.search("ple"))