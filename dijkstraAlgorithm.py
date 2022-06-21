# Define all Nodes with all it's adjecent Nodes with their corresponding wheight
adjecent = {
    "A": [("B", 2), ("D", 8)],
    "B": [("A", 2), ("D", 5), ("E", 6)],
    "C": [("E", 9), ("F", 3)],
    "D": [("A", 8), ("B", 5), ("E", 3), ("F", 2)],
    "E": [("B", 6), ("D", 3), ("F", 1), ("C", 9)],
    "F": [("D", 2), ("E", 1), ("C", 3)]}

# Define a nodeTable where the shortest routes for each nodes are stored
nodeTable = {}
firstLetter = True

for letter in adjecent:
    if firstLetter == True:
        nodeTable[letter] = [0, None]
        firstLetter = False
    else:
        nodeTable[letter] = [10000, None]

notVisited = list(nodeTable.keys())

for node in nodeTable:
    # Make the currentNode the node with the lowest wheigt in the nodeTable
    # Mark this Node as 'visited'
    currentNode = min(notVisited, key=nodeTable.get)
    notVisited.remove(currentNode)

    for pathes in range(len(adjecent[currentNode])):
        pathLetter = adjecent[currentNode][pathes][0]
        totalNewPathWeight = adjecent[currentNode][pathes][1] + \
            nodeTable[currentNode][0]
        oldPathWeight = nodeTable[adjecent[currentNode][pathes][0]][0]

        # If an adjent node from the currentNode is not visted, check if combined wheigt is lower than before.
        if pathLetter in notVisited and totalNewPathWeight < oldPathWeight:
            # If the combined wheight is lower, update the nodeTable with the new shortes route.
            nodeTable[pathLetter][0] = totalNewPathWeight
            nodeTable[pathLetter][1] = currentNode

# Print the table on the screen
print("node:", end="\t\t\t")
for node in nodeTable:
    print(node, end="\t")
print("\nshortest distance:", end="\t")
for node in nodeTable:
    print(nodeTable[node][0], end="\t")
print("\nprevious node:", end="\t\t")
for node in nodeTable:
    print(nodeTable[node][1], end="\t")