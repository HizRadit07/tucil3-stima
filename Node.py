from collections import defaultdict
from math import *

# Node class
class Node:
    def __init__(self, name, x, y):
        # User-Defined Constructor, no need default constructor
        self.name = name
        self.x = x
        self.y = y
        self.neighbors = defaultdict(lambda: "No neighbors")
        self.parent = []
        
    def getDistanceBetween(self, otherNode):
        # Euclidean Distance
        x = self.x - otherNode.x
        y = self.y - otherNode.y
        
        return sqrt(x ** 2 + y ** 2)
    
    def calculateHaversine(self, otherNode):
        # Earth Radius, Get Haversine in KM
        earthRadius = 6371
        
        # Convert Longitude and Latitude to Radians
        lat1 = radians(self.x)
        long1 = radians(self.y)
        lat2 = radians(otherNode.x)
        long2 = radians(otherNode.y)
        # Get the difference
        latDiff = lat2 - lat1
        longDiff = long2 - long1
        # Haversine
        a = (sin(latDiff / 2)**2) + (cos(lat1) * cos(lat2) * sin(longDiff / 2)**2)
        c = 2 * asin(sqrt(a))
        
        return(c* earthRadius)
    
    def printNode(self):
        # Get information from the node
        print("%s (%d, %d)" % (self.name, self.x, self.y))
        print("List of neighbors:")
        for key, value in self.neighbors.items():
            print(key.name, ":", value)
            
    def containsNeighbor(self,node):
        # Check if a node contains other node as neighbors
        for key,value in self.neighbors:
            if (node.name==key.name):
                return True
        return False

    def addParent(self,parentNode):
        # Add the parent of the node
        self.parent.append(parentNode)

    def sortNeighbors(self):
        # Sort neighbors based on Haversine Distance
        self.neighbors = sorted(self.neighbors.items(), key = lambda x: x[1], reverse = False)

    def getParents(self):
        # Get the parents of a node
        if (len(self.parent)!=0):
            return self.parent[0]
        else:
            return []
    def hasParents(self):
        # Check if a node has any parent
        return (len(self.parent)!=0)

    def sameName(self,Node):
        # Check uf two node has same name
        return (self.name==Node.name)