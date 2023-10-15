# root = "A"
# left = "B"
# middle = "E"
# right = "C"

# def graph(left,right,middle,root):
#     this.left = left
#     this.root = root
#     this.middle = middle
#     this.root = root


# #lis a

# def list(data, left,right,)

class Node:
    def __init__(self,state,parent,actions,totalCoast):
        self.state = state
        self.parent = parent
        self.actions = actions
        sefl.totalCoast = totalCoast

graph = {
    'a':Node('a',None, ['b','e','c'],None),
    'b':Node('b',None, ['a','e','d'],None),
    'c':Node('c',None, ['g','f'],None),
    'd':Node('d',None, ['b','e'],None),
    'e':Node('e',None, ['b','a','d'],None),
    'g':Node('g',None, ['c'],None),
    'f':Node('f',None, ['c'],None),
}