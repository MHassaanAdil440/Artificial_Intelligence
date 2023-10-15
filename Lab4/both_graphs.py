# class Node:
    
#     def __init__(self,state,parent,actions,totalCoast):
#         self.state = state
#         self.parent = parent
#         self.actions = actions
#         self.totalCoast = totalCoast

#     # print(self.state)
#     # queue.append(self.actions)
#     # index_of_queue += index_of_queue
#     # print(queue(index_of_queue))

# class MyBfs:

#     def __init__(self,state,parent,actions,totalCoast):
#         frontier = []
#         index_of_queue = 0
#         # self.state = state
#         # self.actions = actions
#         # print(self.state)
#         # queue.append(self.actions)
#         # index_of_queue = index_of_queue + 1
#         # print(queue(index_of_queue))


#         while len(frontier) != 0:
#             currentNode = frontier.pop()
#             explored.append(currentNode)
#             for child in graph3(currentNode).actions:
#                 if child not in frontier and child not in explored:
#                     graph3(child).parent = currentNode
#                     if graph3[child].state == goalstate:
#                         return actionstatement(graph,initialstate, goalstate)
#                     frontier.append(child)

#         print(frontier)

# graph3 = {
#     'a':MyBfs('a',None, ['b','c'],None),
#     'b':MyBfs('b',None, ['d'],None),
#     'c':MyBfs('c',None, ['d','f'],None),
#     'd':MyBfs('d',None, ['d','b','s','e'],None),
#     'e':MyBfs('e',None, ['b','c'],None),
#     's':MyBfs('s',None, ['d','e','p'],None),
#     'p':MyBfs('p',None, ['h','q'],None),
#     'h':MyBfs('h',None, ['p','q'],None),
#     'r':MyBfs('r',None, ['e','f'],None),
#     'f':MyBfs('f',None, ['c','g'],None),
#     'g':MyBfs('f',None, ['f'],None),
#     'q':MyBfs('q',None,['h','p'],None)
# }

# graph2 = {
#     'a':Node('a',None, ['b','c'],None),
#     'b':Node('b',None, ['d'],None),
#     'c':Node('c',None, ['d','f'],None),
#     'd':Node('d',None, ['d','b','s','e'],None),
#     'e':Node('e',None, ['b','c'],None),
#     's':Node('s',None, ['d','e','p'],None),
#     'p':Node('p',None, ['h','q'],None),
#     'h':Node('h',None, ['p','q'],None),
#     'r':Node('r',None, ['e','f'],None),
#     'f':Node('f',None, ['c','g'],None),
#     'g':Node('f',None, ['f'],None),
#     'q':Node('q',Node,['h','p'],None)
# }

# graph1 = {
#     'a':Node('a',None, ['b','e','c'],None),
#     'b':Node('b',None, ['a','e','d'],None),
#     'c':Node('c',None, ['g','f'],None),
#     'd':Node('d',None, ['b','e'],None),
#     'e':Node('e',None, ['b','a','d'],None),
#     'g':Node('g',None, ['c'],None),
#     'f':Node('f',None, ['c'],None),
# }


#write a code in python for bfs and dfs
# for bfs and dfs we need to have a graph
# graph = {
#     'a': ['b','c'],
#     'b': ['d'],
#     'c': ['d','f'],
#     'd': ['d','b','s','e'],
#     'e': ['b','c'],
#     's': ['d','e','p'],
#     'p': ['h','q'],
#     'h': ['p','q'],
#     'r': ['e','f'],
#     'f': ['c','g'],
#     'g': ['f'],
#     'q': ['h','p']
# }

# graph = {
#     'a': ['b','e','c'],
#     'b': ['a','e','d'],
#     'c': ['g','f'],
