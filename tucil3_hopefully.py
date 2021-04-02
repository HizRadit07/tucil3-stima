#Tucil 3 Stima
#Hizkia R. 13519087
#Richard R. 13519185

#node class
class Node:
    def __init__(self,name,x,y):
        self.name = name
        self.x = x
        self.y = y
    def printNode(self):
        print(self.name)
        print(self.x)
        print(self.y)

def getNodeNumber(filename):
    #getting nodeNumber
    readfile = open(filename)
    initNumber = [0]; # get number of nodes first

    for position, line in enumerate(readfile):
        if position in initNumber:
            numOfNodes = int(line) # aquire num of nodes
    return numOfNodes
def getArrayFromFile(column,number,filename):
    #returns array from filename of a specific column
    readfile = open("input2.txt")
    arr = []
    for i,line in enumerate(readfile):
        if i>=1 and i<=number:
            arr.append((line.replace('\n','')).split(' ')[column]);
    return arr;

#-----------------------------------------------------------------------------#
#main#
numOfNodes = getNodeNumber("input2.txt")

readfile = open("input2.txt")
nameArray = getArrayFromFile(0,numOfNodes,"input2.txt");
xArray = getArrayFromFile(1,numOfNodes,"input2.txt");
yArray = getArrayFromFile(2,numOfNodes,"input2.txt");
#will result in 3 arrays of the same size each containing
#name,x,and y, that will be used for nodes

nodeList = []
for i in range (0,(numOfNodes)):
    nodeList.append(Node(nameArray[i],int(xArray[i]),int(yArray[i])));

for i in range (0,len(nodeList)):
    nodeList[i].printNode();




