#Tucil 3 Stima
#Hizkia R. 13519087
#Richard R. 13519185

from flask import Flask, render_template
from Graph import *

#-----------------------------------------------------------------------------#
#main#
if(__name__ == "__main__"):
    filename = "testcase.txt"
    graph = Graph(filename)

    #graph.checkGraph()
    
    # Visualize the graph
    graph.visualize()
    
    solution = [] #array for solution
    startName = input("Please enter the start node: ") #get start name of the node
    goalName = input("Please enter the goal node: ") #get goal name of the node
    if (not graph.isNodeInGraphByName(startName) or (not graph.isNodeInGraphByName(goalName))): #exit immediately if the nodes are not in graph
        print("Sorry, the nodes you are looking for is not in the graph")
        exit()

    goalNode = graph.searchByName(goalName) #goalNode
    startNode = graph.searchByName(startName) #startNode
    solution.append(graph.searchByName(startName)) #add startNode to the solution array
    i = 0
    curNode = solution[i] #init current Node
    curValue = 0 #init starting value as 0
    
    #myNode = getMinimumAStarNode(graph,curNode,goalNode);
    #print (myNode.name)
    while(not containsNode(solution,goalNode)):
        curMinNode = getMinimumAStarNode(graph,curNode,goalNode,curValue) #initiate current Minimum Node
        
        for key,value in curNode.neighbors.items(): #check for each neighbors of current Node
            curMinNode2 = getMinimumAStarNode(graph,key,goalNode,curValue)
            if curMinNode2.getDistanceBetween(goalNode)<=curMinNode.getDistanceBetween(goalNode): #if it is found that the distance between their neighbors and goalnodes are smaller overall
                curMinNode = key #change the curMinNode with the one found in neighbors
                
        solution.append(curMinNode); #append to solution
        curValue = curNode.getDistanceBetween(curMinNode) #change curValue to the value of the path taken
        i+=1
        curNode = solution[i]

    for items in solution:
        print(items.name)

# Flask Try
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def map():
    # filename = "testcase.txt"
    # graph = Graph(filename)
    # points = []
    # for node in graph.nodeList:
    #     coordinates = []
    #     coordinates.append(node.x)
    #     coordinates.append(node.y)
    #     points.append(coordinates)
    points = [[3.5898427621175326, 98.6483296391956], [3.5988800872318683, 98.65249242731477], [3.60012217704572, 98.64172067661467], [3.6062845004961233, 98.65024132694683]]
    
    return render_template('map.html')

if(__name__ == '__main__'):
    app.run(debug = True)