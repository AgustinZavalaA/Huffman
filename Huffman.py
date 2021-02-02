from Node import Node
import os
import shutil

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
            #self.encoTree += "1"
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

    def readNode(self, iter_s):
        c = next(iter_s, -1)
        if c is not -1:
            if c is not "0":
                return Node(data=c)
            else:
                left = self.readNode(iter_s)
                right = self.readNode(iter_s)
                return Node(l=left, r=right)

    def saveFile(self, fName):
        # Writes the tree in a file
        fOut = open(fName + "/" + fName + ".tree", "w")
        fOut.write(self.encoTree)
        fOut.close()
        # writes the encoded text in a different file, it uses the 
        # flag wb to write binaries
        fOut = open(fName + "/" + fName + ".etxt", "wb")
        # This is a little messy, but it converts the encoded text 
        # that is a string of 0 and 1 to binaries with the function 
        # int(x,2) the second parameter convert the string to a binary 
        # number, then with the method to_byte from the int class it
        # creates a byte stream to write in the file 
        fOut.write((int(self.encoText[::-1], 2).to_bytes(int(len(self.encoText)/8)+1, 'little')))
        fOut.close()
        pass

    def decodeText(self, nBits):
        tmp = self.root
        i=0
        for c in self.encoText:
            if tmp.left == None and tmp.right == None:
                print(tmp.data, end="")
                tmp = self.root
            if c == "0":
                tmp = tmp.left
            else:
                tmp = tmp.right
            #i += 1
            #if nBits == i:
            #    break
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
            if opt in (1,2):
                os.system('clear')
                if opt == 1:
                    print("Write text to compress")
                    inputStr = input(">> ")
                else:
                    print("Write direction to text file to compress")
                    inputStr = input(">> ")
                    with open(inputStr, "r") as f:
                        inputStr = f.read()
                self.setFrecuencyTable(inputStr)
                self.setBinaryTree()
                self.setEncodingTable(self.root)
                self.setEncodedString(inputStr)
                self.setEncodedTree(self.root)
                self.encoTree = str(len(inputStr)) + "," + self.encoTree
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
                        print("Descompressed text            ~= %d B" % (len(inputStr)))
                        print("Compressed text (tree + text) ~= %d B" % (len(self.encoTree)+len(self.encoText)/8+1))
                        print("Efficiency                    ~= %.2f" % ((len(inputStr)) / int((len(self.encoTree)+len(self.encoText)/8+1))))
                    if opt2 == 5:
                        fName = input("Write name of archive\n>> ")
                        if os.path.exists(fName):
                            shutil.rmtree(fName)
                        os.mkdir(fName)
                        self.saveFile(fName)
                        break
                    if opt2 == 6:
                        break
                    input("Press enter key to continue...\n")
            elif opt == 3:
                fName = input("Write name of the directory\n>> ")
                with open(fName + "/" + fName + ".etxt" , "rb") as f:
                    textInBytes = f.read()
                with open(fName + "/" + fName + ".tree" , "r") as f:
                    bits        = f.read()
                nChar         = bits.split(sep=",")[0]
                self.encoTree = bits.split(sep=",",maxsplit=1)[1]
                # convert the bits to a string the same way
                self.encoText = format(int.from_bytes(textInBytes, 'little'), str(int(int(nChar)/8)+1) + 'b')[::-1]
                # Creates an iterable to recursively call the next method
                iter_s = iter(self.encoTree)
                self.root = self.readNode(iter_s)
                self.decodeText(nChar)
                input("\nPress enter key to continue...\n")
            else:
                os.system('clear')
                exit()
        pass