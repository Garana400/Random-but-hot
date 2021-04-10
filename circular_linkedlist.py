class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
            return
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        
        new_node = Node(data)
        curr.next = new_node
        new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        curr = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            self.head = new_node
    
    def remove(self, key):
        if self.head:
            curr = self.head
            prev = None
            if curr.data == key:
                if self.head.next == self.head:
                    self.head = None
                else:
                    while curr.next != self.head:
                        curr = curr.next
                    curr.next = self.head.next
                    self.head = self.head.next
            else:    
                while curr.data != key and curr.next != self.head:
                    prev = curr
                    curr = curr.next
                if curr.value == key:
                    prev = curr.next
                    curr = None

    def remove_node(self, node):
        if node:
            curr = node
            prev = None
            while True:
                prev = curr
                curr = curr.next
                if curr == node:
                    break
            if prev != curr:
                prev.next = curr.next
                if curr == self.head:
                    self.head = curr.next
            else:
                self.head = None
            
            curr = None

    
    def split(self):
        size = len(self)
        center = size // 2
        new_list = CircularLinkedList()
        curr = self.head

        while center:
            new_list.append(curr.data)
            curr = curr.next
            center -= 1
        
        new_head = curr
        while curr.next != self.head:
            curr = curr.next
        curr.next = new_head
        self.head = new_head

        return new_list
    
    def josephus_circle(self, step):
        if self.head:
            curr = self.head

            while len(self) > 1:
                count = 1
                while count < step:
                    curr = curr.next
                    count += 1
                print("KILL: ", curr.data)
                self.remove_node(curr)
                curr = curr.next
            return self.head
    
    @staticmethod
    def is_circular_linked_list(input_list):
        curr = input_list.head
        
        while curr and curr.next != input_list.head:
            curr = curr.next
        
        if curr and curr.next == input_list.head:
            return True
        else:
            return False

    def __str__(self):
        cur = self.head 
        output = ""
        while cur:
            output += str(cur.data) + "->"
            cur = cur.next
            if cur == self.head:
                break
        return output[:-2]
    
    def __len__(self):
        count = 0
        curr = self.head

        while curr:
            count += 1
            curr = curr.next
            if curr == self.head:
                break
        
        return count
