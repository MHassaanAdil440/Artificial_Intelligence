class Node:
    def __init__(self,state,parent,actions,totalCoast):
        self.state = state
        self.parent = parent
        self.actions = actions
        sefl.totalCoast = totalCoast

graph = {
    'a':Node('a',None, ['b','c'],None),
    'b':Node('b',None, ['d'],None),
    'c':Node('c',None, ['d','f'],None),
    'd':Node('d',None, ['d','b','s','e'],None),
    'e':Node('e',None, ['b','c'],None),
    's':Node('s',None, ['d','e','p'],None),
    'p':Node('p',None, ['h','q'],None),
    'h':Node('h',None, ['p','q'],None),
    'r':Node('r',None, ['e','f'],None),
    'f':Node('f',None, ['c','g'],None),
    'g':Node('f',None, ['f'],None),
    'q':Node('q',Node,['h','p'],None)
}