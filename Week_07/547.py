class UnionFind:
    def __init__(self):
        self.father = {}
        self.set_num = 0
    
    def find(self,x):
        root = x
        while self.father[root] != None:
            root = self.father[root]
            
        while x != root:
            orginal_father = self.father[x]
            self.father[x],x = root,orginal_father
        
        return root
    
    def merge(self,x,y):
        root_x,root_y = self.find(x),self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            self.set_num -= 1
            
    def add(self,x):
        if x not in self.father:
            self.father[x] = None
            self.set_num += 1
            
class Solution:
    def findCircleNum(self,M):
        uf = UnionFind()
        for i in range(len(M)):
            uf.add(i)
            for j in range(i):
                if M[i][j]:
                    uf.merge(i,j)
        return uf.set_num
    
print(Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))