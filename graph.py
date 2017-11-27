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

    def addEdge(self, v1, v2, weight=1, directed=False):
        if not v1 in self._table.keys():
            self.addVertex(v1)
        self._table[v1].add((v2,weight))
        if not directed:
            if not v2 in self._table.keys():
                self.addVertex(v2)
            self._table[v2].add((v1,weight))

    def removeEdge(self,v1,v2):
        def removeEdge(self, v1, v2, directed=False):
            for (v, w) in self._table[v1]:
                if v == v2:
                    self._table[v1].remove((v, w))
                    break
            if not directed:
                for (v, w) in self._table[v2]:
                    if v == v1:
                        self._table[v2].remove((v, w))
                        break
    def areNeighbours(self, v1, v2):
        if v1 in self._table.keys():
            for (v, w) in self._table[v1]:
                if v == v2:
                    return True
        return False
    def findDFSPath(self, v1, v2, visited = []):
        if self.areNeighbours(v1, v2):
            return [v1, v2]
            # else use BFS..
        if v1 in self._table.keys():
            neighbours = self._table[v1]
            for (n, w) in neighbours:
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

    def cost(self,v1,v2):
        if v1 in self._table.keys():
            for(v,w) in self._table[v1]:
                if v==v2:
                    return w
        return 0

    def findCheapestPath(self, v1, v2, visited=[]):
        if self.areNeighbours(v1, v2):
            return ([v1, v2], self.cost(v1, v2))
        # else use BFS..
        if v1 in self._table.keys():
            neighbours = self._table[v1]
            cheapest_cost = None
            cheapest_path = None
            for (n, w) in neighbours:
                if n not in visited:
                    (p, cost) = self.findCheapestPath(n, v2, visited + [v1])
                    if not cheapest_cost and not cheapest_path:
                        cheapest_cost = cost
                        cheapest_path = p
            if cheapest_path != None:
                return ([v1] + cheapest_path, cheapest_cost + self.cost(v1, cheapest_path[0]))
        return (None, 0)


    def findAllPaths(self, v1, v2, visited = []):
        allpaths = []
        if self.areNeighbours(v1, v2):
            return [[v1, v2]]
            # else use BFS..
        if v1 in self._table.keys():
            neighbours = self._table[v1]

            for (n, w) in neighbours:
                if n not in visited:
                    p = self.findAllPaths(n, v2, visited + [v1])
                    for paths in p:
                        allpaths.append( [v1] + paths)




        return allpaths






