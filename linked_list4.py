class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    
class DoublyLinked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = DoubleNode(value)


        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print("head Node created:", self.head.value)
            return

        new_node.prev = self.tail 
        self.tail.next = new_node
        self.tail = new_node
        print("Appended new Node with value:", self.tail.value)

dllist = DoublyLinked_list()
dllist.append("First Node")

