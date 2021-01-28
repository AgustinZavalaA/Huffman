class Node:
    # constructor
    def __init__(self, w=0, data=""):
        self.data   = data
        self.weight = w
        self.left   = None
        self.right  = None
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

    # utility
    def printTree(self, i=0):
        if self:
            # Print the current node with tabbing to 
            # differenciate the childs from the parent
            print("%s%s" % ("  " * i, self))
            # if the children isn't null recursively print it
            if self.left:
                self.left.printTree(i+1)
            # the same for the right
            if self.right:
                self.right.printTree(i+1)
        pass 
    
    #def searchInTree(self, ch):
    #    pathArray = [0]
    #    if self:
    #        print(pathArray)
    #        if self.left:
    #            pathArray.append("0")
    #            self.left.searchInTree(ch)
#
    #        pathArray.pop()
    #        if self.getData() == ch:
    #            print(pathArray)
    #            return pathArray
#
    #        if self.right:
    #            pathArray.append("1")
    #            self.right.searchInTree(ch)