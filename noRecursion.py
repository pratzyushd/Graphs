#Solution to the graph Problem Set
class graph:
    def __init__(self, value):
        if value:
            self.__dict = value
        else:
            self.__dict = {}


    def addDirectionalEdge(self, newEdge):
        (vertRt, vertLf) = newEdge
        if vertRt in self.__dict:
            self.__dict[vertRt].append(vertLf)
        else:
            self.__dict[vertRt] = [vertLf]

    def addEdge(self, newEdge):
        self.addDirectionalEdge(newEdge)
        self.addDirectionalEdge(newEdge[::-1])

    def printUniqueEdges(self):
        edges = []
        for vert in self.__dict:
            for connector in self.__dict[vert]:
                if [connector, vert] not in edges:
                    edges.append([vert, connector])
        edges.sort()
        return edges

    def printEdges(self):
        edges = []
        for vert in self.__dict:
            for connector in self.__dict[vert]:
                edges.append([vert, connector])
        return edges

    def printVertices(self):
        theKeys = self.__dict.keys()
        verts = []
        for key in theKeys:
            verts.append(key)
        return verts

    def createMatrix(self):
        verts = self.__dict.keys()
        matrix = []
        toprow = ["-"]
        for item in verts:
            toprow.append(item)
        matrix.append(toprow)
        for vert in self.__dict:
            nextVerts = []
            for connector in self.__dict[vert]:
                nextVerts.append(connector)
            nextRow = [vert]
            for vertx in verts:
                if vertx in nextVerts:
                    nextRow.append("X")
                else:
                    nextRow.append("-")
            matrix.append(nextRow)
        return matrix

    def matrixPrint(self):
        print("\n Adjacency Matrix: \n")
        matrix = self.createMatrix()
        for item in matrix:
            print(" ".join(item))
        print("\n")

    def printIt(self):
        print("\nAll Edges:", self.printEdges())
        print("\nUnique Edges:", self.printUniqueEdges())
        print("\nAll Vertices:", self.printVertices())

    def listPrint(self):
        print("\nAdjacency List: ", self.__dict)

graphDict = {"1":["2","3"],
        "2":["1","3"],
        "3":["1","2","4"],
        "4":["3"]
        }
myGraph = graph(graphDict)
myGraph.addEdge(["4","2"])
myGraph.printIt()
myGraph.listPrint()
myGraph.matrixPrint()
