# 1 Create Node
# 2 Create Linked list
# 3 Add Nodes to Linked list
# Print

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  
    
class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, newNode):   
        if self.head is None:     # head=>One Piece->None 
            self.head = newNode
        else:
            lastNode = self.head  # head=>One Piece->JoyBoy->None || One Piece->Roger  
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
    # head=>One piece->JoyBoy->Roger->None   
        if self.head is None:
            print("List in empty")      
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next             

# Node => data, next
firstNode = Node("One Piece")
linkedlist = Linkedlist()
# linkedlist.insert(firstNode)
secondNode = Node("JoyBoy")
# linkedlist.insert(secondNode)
thirdNode = Node("Roger") 
# linkedlist.insert(thirdNode)
linkedlist.printList()

