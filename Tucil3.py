#Tucil 3 Stima
#Hizkia R. 13519087
#Richard R. 13519185

from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx
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
    # Make an Adjacency Matrix
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

# Node class
class Node:
    def __init__(self, name, x, y):
        # User-Defined Constructor, no need default constructor
        self.name = name
        self.x = x
        self.y = y
        self.neighbors = defaultdict(lambda: "No neighbors")
        
    def getDistanceBetween(self, otherNode):
        x = self.x - otherNode.x
        y = self.y - otherNode.y
        
        return math.sqrt(x ** 2 + y ** 2)
                
    def printNode(self):
        # Get information from the node
        print("%s (%d, %d)" % (self.name, self.x, self.y))
        print("List of neighbors:")
        for key, value in self.neighbors.items():
            print(key.name, ":", value)
    def containsNeighbor(self,node):
        for key,value in self.neighbors:
            if (node.name==key.name):
                return True;
        return False;

# Graph Class 
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
            self.nodeList.append(Node(nameArray[i], int(xArray[i]), int(yArray[i])))
        # Set neighbors
        self.setNeighbors(filename)
    
    def setNeighbors(self, filename):
        # Add Neighbors from the list of nodes to the list of neighbors
        adjMatrix = getAdjMatrix(filename)
        
        # Get the corresponding row
        for i in range(len(self.nodeList)):
            dictOfNeighbors = defaultdict(lambda: "No Nodes")
            weightRow = adjMatrix[i]
            for j in range(len(weightRow)):
            # Get the neighbors
                if(weightRow[j] == 1):
                    # Append K: Name of neighbors, V: Edge Weight
                    weight = self.nodeList[i].getDistanceBetween(self.nodeList[j])
                    dictOfNeighbors[self.nodeList[j]] = weight
            self.nodeList[i].neighbors = dictOfNeighbors
    
    def searchByName(self, name):
        # Search a  node based on its name
        for node in self.nodeList:
            if(node.name == name):
                return node
    
    def checkGraph(self):
        # Iterate Node List
        for i in range (0, len(self.nodeList)):
            print("Node %d: " % (i + 1))
            self.nodeList[i].printNode()
            print()
            
    def visualize(self):
        # Create NX Graph
        graph = nx.Graph()
        
        # Iterate each node
        for node in self.nodeList:
            # Add nodes with node names
            graph.add_node(node.name)
            
            # Add edges if not exists in the edge list of NX Graph
            for key, value in node.neighbors.items():
                if(not graph.has_edge(node.name, key.name)):
                    graph.add_edge(node.name, key.name, weight = round(value, 2))
        # Create a layout
        pos=nx.spring_layout(graph)
        # Draw graph nodes
        nx.draw(graph, pos, with_labels = True, font_weight = 'bold')
        edge_weight = nx.get_edge_attributes(graph, 'weight') # Get graph edges weights
        # Draw graph edges
        nx.draw_networkx_edge_labels(graph, pos, edge_labels = edge_weight)
        plt.show()
        
    def isNodeInGraphByName(self,nodeName):
        #find if a Node is in the graph by its name, returns true if yes
        for n in self.nodeList:
            if (n.name==nodeName):
                return True;
        return False;
    
    def searchNodeByNode(self,Node):
        #find a Node by its name
        for n in self.nodeList:
            if (n.name==Node.name):
                return n;


def containsNode(arr,Node):
    #procedure to check if an array contains a node
    for item in arr:
        if (item.name==Node.name and item.x==Node.x and item.y==Node.y):
            return True;
    return False;

def isNeighbors(node1,node2):
    #returns true if node1 and node2 are neighbors
    for key,value in node1.neighbors.items():
        if (key.name==node2.name and key.x==node2.x and key.y==node2.y):
            return True;
    return False;

def getMinimumAStarNode(myGraph, myNode, endNode,currentValue):
    #A Star implementation is here
    #returns node with the minimum distance to goal from myNode
    curMinNode = myNode; #set current minimum node as self
    count = 999999; #set count
    for key,value in myNode.neighbors.items():
        currentNode = myGraph.searchNodeByNode(key)
        curCount = value + currentNode.getDistanceBetween(endNode)+currentValue; #check value + distance between nodes
        if (curCount<count): #if currentCount<count make currentMinimumNode = currentNode
            count = curCount;
            curMinNode = currentNode;
    
    return curMinNode
#-----------------------------------------------------------------------------#
#main#
if(__name__ == "__main__"):
    filename = "testcase.txt"
    graph = Graph(filename)
    
    #graph.checkGraph()
    #graph.visualize()
    solution = [] #array for solution
    startName = input("Please enter the start node: "); #get start name of the node
    goalName = input("Please enter the goal node: "); #get goal name of the node
    if (not graph.isNodeInGraphByName(startName) or (not graph.isNodeInGraphByName(goalName))): #exit immediately if the nodes are not in graph
        print("sorry, the nodes you are looking for is not in the graph");
        exit;

    goalNode = graph.searchByName(goalName); #goalNode
    startNode = graph.searchByName(startName); #startNode
    solution.append(graph.searchByName(startName)); #add startNode to the solution array
    i = 0;
    curNode = solution[i]; #init current Node
    curValue = 0; #init starting value as 0
    
    #myNode = getMinimumAStarNode(graph,curNode,goalNode);
    #print (myNode.name)
    while(not containsNode(solution,goalNode)):
        curMinNode = getMinimumAStarNode(graph,curNode,goalNode,curValue) #initiate current Minimum Node
        
        for key,value in curNode.neighbors.items(): #check for each neighbors of current Node
            curMinNode2 = getMinimumAStarNode(graph,key,goalNode,curValue);
            if curMinNode2.getDistanceBetween(goalNode)<=curMinNode.getDistanceBetween(goalNode): #if it is found that the distance between their neighbors and goalnodes are smaller overall
                curMinNode = key; #change the curMinNode with the one found in neighbors
                
        solution.append(curMinNode); #append to solution
        curValue = curNode.getDistanceBetween(curMinNode); #change curValue to the value of the path taken
        i+=1
        curNode = solution[i]

    for items in solution:
        print(items.name)
        
            
    
