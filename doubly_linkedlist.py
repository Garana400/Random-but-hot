class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
        else:
            self.head = new_node

    def prepend(self, data):
        new_node = Node(data)
        
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
    
    def add_after_node(self, key, data):
        if self.head:
            curr = self.head
            
            while curr and curr.data != key:
                curr = curr.next
            
            if curr and curr.next:
                new_node = Node(data)
                new_node.next = curr.next
                new_node.prev = curr
                curr.next.prev = new_node
                curr.next = new_node
            elif curr:
                self.append(data)
    
    def add_before_node(self, key, data):
        if self.head:
            curr = self.head
            
            while curr and curr.data != key:
                curr = curr.next
            
            if curr and curr.prev:
                new_node = Node(data)
                new_node.next = curr
                new_node.prev = curr.prev
                curr.prev.next = new_node
                curr.prev = new_node
            elif curr:
                self.prepend(data)
    
    def remove(self, key):
        if self.head:
            curr = self.head

            while curr and curr.data != key:
                curr = curr.next
            
            if curr and curr.next and curr.prev:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                curr = None
            elif curr and curr.next:
                curr.next.prev = None
                self.head = curr.next
                curr = None
            elif curr and curr.prev:
                curr.prev.next = None
                curr = None
            elif curr:
                self.head = None
                curr = None
    
    def reverse(self):
        if self.head:
            head = self.head
            curr = self.head.next

            head.prev = head.next
            head.next = None

            while curr:
                nxt = curr.next
                curr.next = curr.prev
                curr.prev = nxt
                if nxt is None:
                    self.head = curr
                curr = nxt
    
    def remove_duplicates(self):
        if self.head:
            curr = self.head
            frq = dict()
            while curr:
                if frq.get(curr.data):
                    nxt = curr.next
                    self.remove(curr.data)
                    curr = nxt
                else:
                    frq[curr.data] = 1
                    curr = curr.next
    
    def pairs_with_sum(self, sum_val):  
        answer = list()
        seen = dict()
        if self.head:
            curr = self.head
            while curr:
                seen[curr.data] = 1
                if seen.get(sum_val - curr.data):
                    answer.append("("+str(sum_val-curr.data)  +","+str(curr.data) + ")")
                curr = curr.next
        return answer

    def __str__(self):
        curr = self.head
        output = ""

        while curr:
            output += str(curr.data) + " -> "
            curr = curr.next
        
        return output[:-3]
