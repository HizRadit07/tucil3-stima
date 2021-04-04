from collections import defaultdict
import math

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
                return True
        return False

    def addParent(self,parentNode):
        self.parent.append(parentNode)

    def sortNeighbors(self):
        self.neighbors = sorted(self.neighbors.items(),key=lambda x:x[1],reverse=False)

    def getParents(self):
        if (len(self.parent)!=0):
            return self.parent[0]
        else:
            return []
    def hasParents(self):
        return (len(self.parent)!=0)