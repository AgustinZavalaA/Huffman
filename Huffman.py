from Node import Node
import os

class Huffman:
    def __init__(self):
        self.root      = Node()
        self.frecTable = {}
        self.encoTable = {}
        self.encoText  = ""
        self.encoTree  = ""
        pass

    def setFrecuencyTable(self, s):
        # Get all the characters from a given string.
        # if it find it in the dictionary "frecTable"
        # it will add 1 to the frecuency if the char
        # is new to the table it will set it to 1
        # so the next time it is encountered it will 
        # add 1 otherwise it wont start the dictionary
        for c in s:
            if c in self.frecTable:
                self.frecTable[c] += 1
            else:
                self.frecTable[c] = 1
        # Sort the dictionary
        self.frecTable = dict(sorted(self.frecTable.items(), key=lambda item: item[1]))
        pass

    def setEncodingTable(self, node, path=[], append=2):
        # this method create the encoding table 
        # it traverse the binary tree from root 
        # to leaf, when it encounters a leaf it 
        # save the encoding table
        if node is None:
            return
        path.append(append)

        if node.left is None and node.right is None:
            self.encoTable[node.data] = path[1:]
    
        self.setEncodingTable(node.left, path, 0)
        self.setEncodingTable(node.right, path, 1)
    
        path.pop()
        pass

    def setEncodedString(self, inputStr):
        for c in inputStr:
            # This line append every char in the
            # input string but it also replace every
            # bracket comma and space
            self.encoText += str(self.encoTable[c])
            self.encoText = self.encoText.translate({ord(i): None for i in "[], "})
        pass

    def setEncodedTree(self, node):
        if node is None:
            return
        if node.left is None and node.right is None:
            self.encoTree += "1"
            self.encoTree += node.data
        else:
            self.encoTree += "0"
            self.setEncodedTree(node.left)
            self.setEncodedTree(node.right) 
        pass

    def printFrecuencyTable(self):
        for key, value in self.frecTable.items():
            print("%c : %d" % (key, value))
        pass

    def printEncodingTable(self):
        for key, value in self.encoTable.items():
            print("%c : %s" % (key, str(value)))
        pass

    def printEncodedString(self, inputStr):
        print("\"%s\" Is equivalent to \n%s" % (inputStr, self.encoText))
        pass

    def printEncodedTree(self):
        print("Encoded Tree = %s" % self.encoTree)

    def setBinaryTree(self):
        Forest = []
        for key, value in self.frecTable.items():
            Forest.append(Node(value, key))
        while len(Forest) > 1:
            newNode = Node(Forest[0].getWeight() + Forest[1].getWeight())
            if Forest[0].getWeight() > Forest[1].getWeight():
                newNode.left  = Forest[1]
                newNode.right = Forest[0]
            else:
                newNode.left  = Forest[0]
                newNode.right = Forest[1]
            Forest = Forest[2:]
            Forest.append(newNode)
            Forest.sort(key=lambda n: n.weight)
        #print(Forest[0])
        #print(Forest)
        self.root = Forest[0]

        pass

    def menu(self):
        while True:
            self.root      = Node()
            self.frecTable = {}
            self.encoTable = {}
            self.encoText  = ""
            self.encoTree  = ""
            os.system('clear')
            print("****  Menu  *****")
            print("1.- Compress   Input Text")
            print("2.- Compress   File  Text")
            print("3.- Decompress File")
            print("4.- Exit")
            opt = int(input(">> "))
            while opt < 1 or opt > 4:
                opt = int(input("Wrong option. Try again\n>> "))
            if opt == 1:
                os.system('clear')
                print("Write text to compress")
                inputStr = input(">> ")
                self.setFrecuencyTable(inputStr)
                self.setBinaryTree()
                self.setEncodingTable(self.root)
                self.setEncodedString(inputStr)
                self.setEncodedTree(self.root)
                while True:
                    os.system('clear')
                    print("1.- Show frecuency table")
                    print("2.- Show binary tree")
                    print("3.- Show char encoding")
                    print("4.- Show efficiency")
                    print("5.- Save to file")
                    print("6.- Exit without saving")
                    opt2 = int(input(">> "))
                    os.system('clear')
                    while opt2 < 1 or opt2 > 6:
                        opt2 = int(input("Wrong option. Try again\n>> "))
                    if opt2 == 1:
                        self.printFrecuencyTable()
                    if opt2 == 2:
                        self.root.printTree()
                        self.printEncodedTree()
                    if opt2 == 3:
                        self.printEncodingTable()
                        self.printEncodedString(inputStr)
                    if opt2 == 4:
                        print()
                    if opt2 == 5:
                        break
                    if opt2 == 6:
                        break
                    input("Press enter key to continue...\n")

            elif opt == 2:
                print()
            elif opt == 3:
                print()
            else:
                os.system('clear')
                exit()
        pass


