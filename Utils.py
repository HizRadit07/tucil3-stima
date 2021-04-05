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

def containsNode(arr,Node):
    # Procedure to check if an array contains a node
    for item in arr:
        if (item.name==Node.name and item.x==Node.x and item.y==Node.y):
            return True
    return False

def isNeighbors(node1,node2):
    # Returns true if node1 and node2 are neighbors
    for key,value in node1.neighbors.items():
        if (key.name==node2.name and key.x==node2.x and key.y==node2.y):
            return True
    return False

def getMinimumAStarNode(myGraph, myNode, endNode,currentValue):
    # A Star implementation is here (hopefully, can change)
    # Returns node with the minimum distance to goal from myNode
    curMinNode = myNode; #set current minimum node as self
    count = 999999; #set count
    for key,value in myNode.neighbors.items():
        currentNode = myGraph.searchNodeByNode(key)
        curCount = value + currentNode.calculateHaversine(endNode)+currentValue; #check value + distance between nodes
        if (curCount<count): #if currentCount<count make currentMinimumNode = currentNode
            count = curCount
            curMinNode = currentNode
    
    return curMinNode

def is_in_queue(x,q):
    # Check if a node is in the queue
    for items in q.queue:
        if (items[1].name==x.name):
            return True
    return False

def findInQueue(x,q):
    # Find a node in the queue
    for items in q.queue:
        if(items[1].name==x.name):
            return items[1]
    return None
