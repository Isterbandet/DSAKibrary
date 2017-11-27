class Graph:
    def __init__(self):
        self._table = {}

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self._table.keys())

    def addVertex (self, v):
        if v not in self._table.keys():
            self._table[v] = set([])

    def removeVertex(self, v):
        if v in self._table.keys():
            del self._table[v]

    def addEdge(self, v1, v2, weight):
        if not v1 in self._table.keys():
            self.addVertex((v1, weight))
        self._table[v1].add(v2)
        if not v2 in self._table.keys():
            self.addVertex((v2, weight))
        self._table[v2].add(v1)

    def removeEdge(self,v1,v2):
        if v2 in self._table[v1]:
            self._table[v1].remove(v2)
        if v1 in self._table[v2]:
            self._table[v2].remove(v1)

    def areNeighbours(self, v1, v2):
        return v2 in self._table[v1]

    def findDFSPath(self, v1, v2, visited = []):
        if self.areNeighbours(v1,v2):
            return [v1,v2]

        for n in self._table[v1]:
            if n not in visited:
                p = self.findDFSPath(n, v2, visited + [v1])
                
                if p != None:
                    return [v1] + p


        return None

    def isConnected(self):
        for v1 in self._table.keys():
            for v2 in self._table.keys():
                if v1 != v2 and not self.findDFSPath(v1,v2):
                    return False
        return True







