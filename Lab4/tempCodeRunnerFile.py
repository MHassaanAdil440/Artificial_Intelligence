 while len(frontier) != 0:
            currentNode = frontier.pop()
            explored.append(currentNode)
            for child in graph3(currentNode).actions:
                if child not in frontier and child not in explored:
                    graph3(child).parent = currentNode
                    if graph3[child].state == goalstate:
                        return actionstatement(graph,initialstate, goalstate)
                    frontier.append(child)
