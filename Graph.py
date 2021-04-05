import matplotlib.pyplot as plt
import networkx as nx
from Utils import *
from Node import *

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
            self.nodeList.append(Node(nameArray[i], float(xArray[i]), float(yArray[i])))
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
                    weight = self.nodeList[i].calculateHaversine(self.nodeList[j])
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
                return True
        return False
    
    def searchNodeByNode(self,Node):
        #find a Node by its name
        for n in self.nodeList:
            if (n.name==Node.name):
                return n
            
    def getPoints(self):
        points = []
        for node in self.nodeList:
            nodePoint = []
            nodePoint.append(node.x)
            nodePoint.append(node.y)
            nodePoint.append(node.name)
            points.append(nodePoint)
        return points
    
    def showAllPlaces(self):
        print("List of available places: ")
        for node in self.nodeList:
            print(node.name)
        print()