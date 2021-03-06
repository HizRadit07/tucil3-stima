#Tucil 3 Stima
#Hizkia R. 13519087
#Richard R. 13519185

# Import Libraries
from flask import Flask, render_template
from queue import PriorityQueue
from Graph import *

def printqueue(q):
    for items in q.queue:
        if (not items[1].hasParents()):
            print("No items in the queue!")
        else:
            print (str(items[0])+ " node " + items[1].name+ " with parent " + items[1].getParents().name)
# A* Algorithm
def AStarSearch(graph, goalName, startName):
    solution = PriorityQueue() #priority queue for solution
    with solution.mutex:
        solution.queue.clear() #make sure we always start on an empty queue

    graph.removeAllNodeParent() #make sure all the nodes also has empty parents

    solution2 = [] #array for solution 2
    
    goalNode = graph.searchByName(goalName) # goalNode
    startNode = graph.searchByName(startName) # startNode
    solution.put((0, startNode))
    i = -1
    #print(curNode[1].name)
    while(not is_in_queue(goalNode, solution) and i<len(solution.queue)):
        i+=1
        if (i>=len(solution.queue)): #protection againts not found
            break
        curNode = solution.queue[i]

        for j in range (0,i): #guard for elements that are inserted before curNode
            for key,value in solution.queue[j][1].neighbors.items():
                if (not is_in_queue(key, solution)):
                    key.addParent((solution.queue[j])[1])
                    solution.put((key.calculateHaversine(goalNode)+ value+key.getDistanceBetween(goalNode), key))

        for key,value in curNode[1].neighbors.items():
            if (not is_in_queue(key, solution)):
                key.addParent(curNode[1])
                solution.put((key.calculateHaversine(goalNode)+ value, key)) #the a star portion of the code
        
        solution.queue.sort()

    # Heuristic, if iteration count is bigger than the size of the graph, no solution is available
    # Not found
    if (i>=len(solution.queue)):
        return []
            
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

# Read file and create a graph
def getGraphFromFile():
    # Init boolean to flag if file is found
    foundFile = False
    
    # Repeat until a file is loaded successfully
    while(not foundFile):
        try:
            # Create a graph based on the files
            filename = input("Enter the name of the file you want to read: ")
            graph = Graph(filename)
            foundFile = True
        except:
            print("No file found!\n")
    
    return graph
    #graph.checkGraph()

def visualize(graph, miscList):
    check = int(input("Choose 1 to visualize with NetworkX, 2 with HERE Maps API, and 3 for to use both sequentially: "))
    if(check == 1):
        # Visualize with NetworkX
        graph.visualize(miscList)
    elif(check == 2):
        # Visualize with HERE Map API through Flask
        print("Follow the local link to see HERE Map API Visualization!")
        print("Use CTRL-C to restart!\n")
        app.run(debug = False)
    elif(check == 3):
        # NetworkX and HERE
        graph.visualize(miscList)
        print("Follow the local link to see HERE Map API Visualization!")
        print("Use CTRL-C to restart!\n")
        app.run(debug = False)
    else:
        print("Invalid Input! Canceling Visualization!")

# Init Flask for HERE MAPS API
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def map():
    # Get points
    points = graph.getPoints()
    
    # Get solution from A* Search
    solution = AStarSearch(graph, goalName, startName)
    
    # To be able to pass into JS, the elements shouldn't be object
    # Insert informations about the node to the path list
    path = []
    for node in solution:
        sols = []
        sols.append(node.x)
        sols.append(node.y)
        sols.append(node.name)
        path.append(sols)
        
    # Render the template of map and pass the lists
    return render_template('map.html', points = points, path = path)

#-----------------------------------------------------------------------------#
# Main Program

# Init read file
graph = getGraphFromFile()

# Visualize the full graph with NetworkX
graph.visualize([])
#graph.checkGraph()

# Repeat until the user wants to exit the program
while(True):
    
    # Request input from the user
    print()
    choice = int(input("Enter 1 to proceed to A*, 2 to reinput the file, 3 to exit the program: "))
    
    # Commence A* Processes
    if(choice == 1):
        print("Entering A* Process...\n")
        graph.showAllPlaces()
        startName = input("Please enter the start node: ") # Get start name of the node
        goalName = input("Please enter the goal node: ")   # Get goal name of the node

        if (not graph.isNodeInGraphByName(startName) or (not graph.isNodeInGraphByName(goalName))): # Node(s) is not in graph
            print("Sorry, the node(s) you are looking for is not in the graph!")
        elif(startName == goalName):
            print("You entered same names. We cannot move!") # Same start and goal node
        else:
            solution = AStarSearch(graph, goalName, startName) # Find The Closest Path with A Star

            if (len(solution) == 0): # Check if solution not found
                print ("NO PATH IS FOUND")
            else:
                # Print the path
                print("FOUND A PATH!")
                print("Closest path from", startName, "to", goalName, "is:")
                for nodes in solution[:-1]:
                    print(nodes.name, end = " => ")
                print(solution[-1].name)
                print()
                
                visualize(graph, solution)
                
    # Commence read file again
    elif(choice == 2):
        graph = getGraphFromFile()
        graph.visualize([])
    # Exit the program
    elif(choice == 3):
        print("Thank you! !_!")
        exit()
    # Invalid choices
    else:
        print("Invalid Input! Try again.")
