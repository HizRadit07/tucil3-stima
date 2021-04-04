#Tucil 3 Stima
#Hizkia R. 13519087
#Richard R. 13519185

from flask import Flask, render_template
from Graph import *
from queue import PriorityQueue

#-----------------------------------------------------------------------------#
#main#
if(__name__ == "__main__"):
    filename = "testcase.txt"
    graph = Graph(filename)

    #graph.checkGraph()
    
    # Visualize the graph
    #graph.visualize()
    
    solution = PriorityQueue() #priority queue for solution 
    solution2 = []
    startName = input("Please enter the start node: ") #get start name of the node
    goalName = input("Please enter the goal node: ") #get goal name of the node
    if (not graph.isNodeInGraphByName(startName) or (not graph.isNodeInGraphByName(goalName))): #exit immediately if the nodes are not in graph
        print("Sorry, the nodes you are looking for is not in the graph")
        exit()

    goalNode = graph.searchByName(goalName) #goalNode
    startNode = graph.searchByName(startName) #startNode
    solution.put((0,startNode))
    i = 0
    curNode = solution.queue[i]
    #print(curNode[1].name)
    while(not is_in_queue(goalNode,solution)):
        for key,value in curNode[1].neighbors.items():
            if (not is_in_queue(key,solution)):
                key.addParent(curNode[1])
                solution.put((key.getDistanceBetween(goalNode)+value,key))
        i+=1
        curNode = solution.queue[i]
    
    for items in solution.queue:
        print(items[1].name,end= ' with parents: ')
        if (items[1].hasParents()):
            print(items[1].getParents().name)
        else:
            print(items[1].getParents())
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
