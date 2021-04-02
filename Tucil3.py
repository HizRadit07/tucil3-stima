#Tucil 3 Stima
#Hizkia R. 13519087
#Richard R. 13519185

from collections import defaultdict
import math

def getNodeNumber(filename):
    # Getting the number of nodes
    source = open(filename)
    initNumber = [0]; # get number of nodes first

    for position, line in enumerate(source):
        if position in initNumber:
            numOfNodes = int(line) # acquire num of nodes
    return numOfNodes

def getArrayFromFile(column, number, filename):
    #returns array from filename of a specific column
    source = open(filename)
    arr = []

    for i, line in enumerate(source):
        if i >= 1 and i <= number:
            arr.append((line.replace('\n','')).split(' ')[column])
    return arr

def getAdjMatrix(filename):  
    # Make a Adjacency Matrix
    adjMatrix = []
    
    # Open and get number of nodes from the file
    source = open(filename)
    numOfNodes = getNodeNumber(filename)
    
    # Enumerate the files and iterate
    for position, line in enumerate(source):
        line = line.replace('\n','').split(' ') # Clean the file
        row = []
        if(position >= numOfNodes + 1):
            for weight in line:
                row.append(int(weight)) # Get each row of the file containing weights
            adjMatrix.append(row) # Append to the matrix
    
    return adjMatrix

#node class
class Node:
    def __init__(self, name, x, y, neighbors):
        # User-Defined Constructor, no need default constructor
        self.name = name
        self.x = x
        self.y = y
        self.neighbors = neighbors
        
    def getDistanceBetween(self, otherNode):
        x = self.x - otherNode.x
        y = self.y - otherNode.y
        
        return math.sqrt(sum(x ** 2 + y ** 2))
                
    def printNode(self):
        # Get information from the node
        print("%s (%d, %d)" % (self.name, self.x, self.y))
        print("List of neighbors:")
        for key, value in self.neighbors.items():
            print(key, ":", value)
        
class Graph:
    def __init__(self, filename):
        self.nodeList = []
        
        # Number of nodes from the source
        numOfNodes = getNodeNumber(filename)
        #will result in 3 arrays of the same size each containing
        #name,x,and y, that will be used for nodes
        nameArray = getArrayFromFile(0, numOfNodes, filename)
        xArray = getArrayFromFile(1, numOfNodes, filename)
        yArray = getArrayFromFile(2, numOfNodes, filename)
        
        # Append the nodes to nodeList
        for i in range (0, (numOfNodes)):
            neighbors = self.getNeighbors(filename, i, nameArray)
            self.nodeList.append(Node(nameArray[i], int(xArray[i]), int(yArray[i]), neighbors))
    
    @staticmethod # Decorators
    def getNeighbors(filename, idxOfNodes, listOfNodes):
        # Add Neighbors from the list of nodes to the list of neighbors
        adjMatrix = getAdjMatrix(filename)
        dictOfNeighbors = defaultdict(lambda: "No Nodes")
        
        # Get the corresponding row
        weightRow = adjMatrix[idxOfNodes]
        for i in range(len(weightRow)):
            # Get the neighbors
            if(weightRow[i] > 0):
                # Append K: Name of neighbors, V: Edge Weight
                dictOfNeighbors[listOfNodes[i]] = weightRow[i]
        
        return dictOfNeighbors
    
    def checkGraph(self):
        # Iterate Node List
        for i in range (0, len(self.nodeList)):
            print("Node %d: " % (i + 1))
            self.nodeList[i].printNode()
            print()

#-----------------------------------------------------------------------------#
#main#
filename = "testcase.txt"
graph = Graph(filename)

graph.checkGraph()