class Node:
    # constructor
    def __init__(self, w=0, data="",l=None, r=None):
        self.data   = data
        self.weight = w
        self.left   = l
        self.right  = r
        pass

    def __str__(self):
        return "data = %s w = %4d" % (self.data, self.weight)

    # getters
    def getData(self):
        return self.data

    def getWeight(self):
        return self.weight

    # setters
    def setData(self, d):
        self.data = d
        pass

    def setWeight(self, w):
        self.weight = w
        pass

    def setLeft(self, n):
        self.left = n
        pass

    def setRight(self, n):
        self.right = n
        pass

    # utility
    def printTree(self, i=0):
        if self:
            # Print the current node with tabbing to 
            # differenciate the childs from the parent
            print("%s%s" % ("  " * i, self))
            # if the left children isn't null recursively print it
            if self.left:
                self.left.printTree(i+1)
            # the same for the right
            if self.right:
                self.right.printTree(i+1)
        pass 