import sys


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxsize
        self.visited = False
        self.previous = None

    def addNeighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def getConnections(self):
        return self.adjacent.keys()

    def getVertexId(self):
        return self.id

    def getWeight(self, neighbor):
        return self.adjacent[neighbor]

    def getDistance(self):
        return self.distance

    def getVisited(self):
        return self.visited

    def getPrevious(self):
        return self.previous

    def setDistance(self, distance):
        self.distance = distance

    def setVisited(self):
        self.visited = True

    def setPrevioud(self, previous):
        self.previous = previous

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent.keys()])


class Graph:
    def __init__(self):
        self.vertexDict = {}
        self.numVertices = 0

    def __iter__(self):
        return iter(self.vertexDict.values())

    def addVertex(self, node):
        newVertex = Vertex(node)
        self.vertexDict[node] = newVertex
        self.numVertices += 1
        return newVertex

    def addEdge(self, frm, to, cost=0):
        if frm not in self.vertexDict:
            self.addVertex(frm)

        if to not in self.vertexDict:
            self.addVertex(to)

        self.vertexDict[frm].addNeighbor(self.vertexDict[to], cost)
        # For directed graoh do not add this.
        self.vertexDict[to].addNeighbor(self.vertexDict[frm], cost)

    def getEdges(self):
        edgeList = []
        for frm in self.vertexDict.values():
            weight = 0
            for to in frm.getConnections():
                weight = frm.getWeight(to)
                edgeList.append((frm.getVertexId(), to.getVertexId(), weight))
        return edgeList


def DFS(currentVert, visited={}):
    visited[currentVert] = True
    print(f"visited :{currentVert.getVertexId()}")  # output

    for neighbor in currentVert.getConnections(): # b, c
        if neighbor not in visited:  # Breaking condition
            DFS(neighbor, visited)



def DFSTraversal(G):
    # First travel each node
    # keep a flag keeper like visited = {}
    # call to a function that function will call itself recursively.
    # 
    visited = {}
    for currentVert in G:  # a, b, c, d
        if currentVert not in visited:
            DFS(currentVert, visited)



if __name__ == '__main__':
    print("Hello")

    G = Graph()
    G.addVertex('a')
    G.addVertex('b')
    G.addVertex('c')
    G.addVertex('d')
    G.addVertex('e')
    G.addVertex('f')
    G.addEdge('a', 'b', 1)
    G.addEdge('a', 'c', 1)
    G.addEdge('b', 'd', 1)
    G.addEdge('b', 'e', 1)
    G.addEdge('c', 'd', 1)
    G.addEdge('c', 'e', 1)
    G.addEdge('d', 'e', 1)
    G.addEdge('e', 'a', 1)
    print('Graph Data:')
    print(G.getEdges())
    print(G.vertexDict)

    DFSTraversal(G)



    # Space complexity: O(N) + O(N) + O(N) = O(3N) ~ O(N), Space for DFS stack space, visited array, adjacency list.
    # Time complexity: for Undirected Graph:
    #       O(N) + summation of degrees = O(N) + 2E,
    #       O(N) -- calling recursion function once for each node.
    #       2E: for each node it is number of adjacent neighbours + number of adjacent neighbours + number of adjacent neighbours etc...
    #           = degree of node + degree of node + degree of node ... = summation of degrees = 2E

    # Time complexity: for Directed Graph: O(N) + E -- no of edges.