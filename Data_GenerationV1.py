#VERSION 1 of Data Generation

#list of packages START

import networkx as networkx
import matplotlib.pyplot as plot
import random
import os

#list of packages END

#goal is to generate a 20 by 20 graph randomly

def generateGraph(filePath):

    #generates x number of nodes from 3 <= x <= 10
    randomNodes = random.randint(3, 10)
    graph = networkx.Graph()
    graph.add_nodes_from(range(randomNodes))

    #now we have to give those nodes a xy coordinate in said graph

    pos = {}

    for node in range(randomNodes):
        x_coord = random.randint(0,20)
        y_coord = random.randint(0,20)
        pos[node] = (x_coord,y_coord)

    #now we have to connect the nodes with weights

    for node in range(randomNodes):
        for j in range(node + 1, randomNodes):

            #the weight in context of my project will depict time
            weight = random.randint(1,10)
            graph.add_edge(node, j, weight=weight)


    #time to configure matplotlib figure

    #change this if the box is too small or too big for your needs
    figure = plot.figure(figsize=(8,8))
    axes = plot.gca()

    axes.set_xlim(-1,30)
    axes.set_ylim(-1,30)

    axes.set_xticks(range(-1,30, 1))
    axes.set_yticks(range(-1, 30, 1))


    weight_list = []

    for x, y in graph.edges():
        current_weight = graph[x][y]['weight']
        weight_list.append(current_weight)


    #time to draw!...

    networkx.draw_networkx_nodes(graph, pos, node_size=250, node_color='cyan')
    networkx.draw_networkx_edges(graph, pos, width=weight_list, edge_color='green')
    networkx.draw_networkx_labels(graph, pos, font_color='black', font_weight='bold')

    plot.title("20 by 20 graph - randomly generated")
    plot.xlabel("x coords")
    plot.ylabel("y coords")
    
    #saving data

    plot.savefig(filePath, format='jpg', dpi=100, bbox_inches='tight')
    plot.close(figure)


# now to actually run and save images for data collection

#saves the training data in the downloads directory for user
home_DIR = os.path.expanduser('~')
download_DIR = os.path.join(home_DIR, 'Downloads', 'dataset')
runs = 100

#if user does not have the dataset folder already created
os.makedirs(download_DIR, exist_ok=True)

#runs the program for x amount of times and saves each "run" into the datasets folder
for run in range(runs):
    file_name = os.path.join(download_DIR, f"graph_{run}.jpg")
    generateGraph(file_name)
    print(f"{file_name} downloaded")

print("generation done.")
