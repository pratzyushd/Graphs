#Solution to the graph Problem Set - Non-Recursive Adjacency List Method
#Creates a class to be used for the graph
class graph:
#Class initialisation (Creates a dicitonary, either passed, or defaulted to empty)
    def __init__(self, value):
        if isinstance(value, dict):
            self.__dict = value
        else:
            self.__dict = {}

#Procedure used to add a uni-directional edge to the list
    def addDirectionalEdge(self, newEdge):
        vertRt, vertLf = newEdge
#If the vertex is in the dictionary, the new edge is added
        if vertRt in self.__dict:
            self.__dict[vertRt].append(vertLf)
#Otherwise the vertex is added to the dictionary
        else:
            self.__dict[vertRt] = [vertLf]
#Used to sort the connector vertices
        for vert in self.__dict:
            sorter = self.__dict[vert]
            adder = sorted(sorter)
            self.__dict[vert] = adder


#Procedure used to add a non-directional edge to the list
    def addEdge(self, newEdge):
#Uses addDirectionalEdge to add the regular and reverse of the edge to the list
        self.addDirectionalEdge(newEdge)
        self.addDirectionalEdge(newEdge[::-1])


#Function used to return all of the different multi-directional paths available (No reverse instances)
    def printUniqueEdges(self):
#Return List
        edges = []
#Goes through each key in the dictionary
        for vert in self.__dict:
#Goes through each definition in the key
            for connector in self.__dict[vert]:
#Checks if the edge is already in the return list, if not, the edge is added
                if [connector, vert] not in edges:
                    edges.append([vert, connector])
        return edges

#Function used to return all of the possible edge routes
    def printEdges(self):
#Uses the same method as printUniqueEdges, except adds every edge rather than checking for reverse instances
        edges = []
        for vert in self.__dict:
            for connector in self.__dict[vert]:
                edges.append([vert, connector])
        return edges

#Function used to return all of the vertices (Keys in the dictionary)
    def printVertices(self):
#.keys() used to take all of the keys within the dictionary in list form
        theKeys = self.__dict.keys()
        verts = []
        for key in theKeys:
            verts.append(key)
        return verts

#Function used to convert an adjacency list into an adjacency matrix
#EASILY EDITED TO ALLOW FOR WEIGHTED EDGES
    def createMatrix(self):
        verts = self.__dict.keys()
#Uses nested lists (2D Array) to correctly format the matrix
        matrix = []
#Creates the top row
        toprow = ["-"]
        for item in verts:
            toprow.append(item)
        matrix.append(toprow)
#Goes through each key in the dictionary
        for vert in self.__dict:
#List to contain all the linked vertices
            nextVerts = []
#Adds the connecting vertices to the list
            for connector in self.__dict[vert]:
                nextVerts.append(connector)
#Sets the key for the next row in the matrix
            nextRow = [vert]
#Checks if there is an edge linking each vertex, if yes an "x" is printed, otherwise an "-"
#This is the portion of the code that can be edited should we be required to work with weighted lists
            for vertx in verts:
                if vertx in nextVerts:
                    nextRow.append("X")
                else:
                    nextRow.append("-")
#Adds the next row to the matrix, to create the 2D array
            matrix.append(nextRow)
        return matrix

#Procedure used to print the matrix in the correct format
    def matrixPrint(self):
        print("\nAdjacency Matrix: \n")
#Creates the matrix
        matrix = self.createMatrix()
#Uses iteration to print each line
        for line in matrix:
            print(" ".join(line))


#Procedures used to print all of the different combinations of edges and vertices

    def printEds(self):
#All possible edges
        print("\nAll Edges:")
        for line in self.printEdges():
            print (line[0], ",", line[1])

    def printUnEds(self):
#All unique edges (No reverse instances)
        print("\nUnique Edges:")
        for line in self.printUniqueEdges():
            print (line[0], ",", line[1])

    def printVerts(self):
#All vertices
        print("\nAll Vertices:")
        for item in self.printVertices():
            print (item)


#Procedure used to print the adjacency list
    def listPrint(self):
#Uses nested lists (2D arrays) to properly format the list
        returner = []
#Goes through each key in the dictionary, and adds all of the connecting vertices to the list
        for vert in self.__dict:
            printer = [vert, ":"]
            for connector in self.__dict[vert]:
                printer.append(connector)
            returner.append(printer)
        print("\nAdjacency List:\n")
#Displays the list in the correct format
        for line in returner:
            print(" ".join(line))


#TESTING
graphDict = {"1":["2","3"],
        "2":["1","3"],
        "3":["1","2","4"],
        "4":["3"]
        }
myGraph = graph(graphDict)
myGraph.addEdge(["4","2"])
myGraph.printEds()
myGraph.printUnEds()
myGraph.printVerts()
myGraph.matrixPrint()
myGraph.listPrint()
