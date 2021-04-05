#Tucil 3 Stima
#Hizkia R. 13519087
#Richard R. 13519185

from flask import Flask, render_template
from queue import PriorityQueue
from Graph import *

def AStarSearch(graph, goalName, startName):
    solution = PriorityQueue() #priority queue for solution 
    solution2 = []
    
    goalNode = graph.searchByName(goalName) #goalNode
    startNode = graph.searchByName(startName) #startNode
    solution.put((0, startNode))
    i = 0
    curNode = solution.queue[i]
    #print(curNode[1].name)
    while(not is_in_queue(goalNode, solution)):
        for key,value in curNode[1].neighbors.items():
            if (not is_in_queue(key, solution)):
                key.addParent(curNode[1])
                solution.put((key.calculateHaversine(goalNode) + value, key))
        i+=1
        curNode = solution.queue[i]
    
    finalGoalNode = findInQueue(goalNode,solution)  #get the final goal node (with the parent)

    #print(finalGoalNode.getParents())
    while(finalGoalNode.hasParents()):
        solution2.append(finalGoalNode)
        finalGoalNode = findInQueue(finalGoalNode.getParents(),solution)
    #endwhile
    solution2.append(finalGoalNode)
    solution2.reverse()
    #solution2 is now the array containing the path for the graph
    return solution2

# Flask for HERE MAPS API
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
    points = graph.getPoints()
    return render_template('map.html', points = points)

#-----------------------------------------------------------------------------#
# Call the main Program to run the program
#main#

foundFile = False

while(not foundFile):
    try:
        filename = input("Enter the name of the file you want to read: ")
        graph = Graph(filename)
        foundFile = True
    except:
        print("No file found!\n")

#graph.checkGraph()

# Visualize the graph
print("Successfully read the file. Close the NetworkX Visualization to Continue.")
graph.visualize()

while(True):
    choice = int(input("Enter 1 to proceed to A*, 2 to exit the program: "))
    
    if(choice == 1):
        print("Entering A* Process...\n")
        graph.showAllPlaces()
        startName = input("Please enter the start node: ") #get start name of the node
        goalName = input("Please enter the goal node: ") #get goal name of the node

        if (not graph.isNodeInGraphByName(startName) or (not graph.isNodeInGraphByName(goalName))): #exit immediately if the nodes are not in graph
            print("Sorry, the node(s) you are looking for is not in the graph!")
        elif(startName == goalName):
            print("You entered same names. We cannot move!")
        else:
            solution = AStarSearch(graph, goalName, startName)

            for items in solution: #for testing
                print(items.name)
                
            points = graph.getPoints()
            app.run(debug = False)
    else:
        print("Thank you! !_!")
        exit()