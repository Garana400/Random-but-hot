class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print("Previous node does not exist.")
            return 

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):

        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None 
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return 

        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):

        cur_node = self.head

        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        count = 1
        while cur_node and count != pos:
            prev = cur_node 
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return 

        prev.next = cur_node.next
        cur_node = None

    def len_iterative(self):

        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count
    
    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)
    
    def swap(self, key_1, key_2):
        if key_1 == key_2:
            return
        
        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.value != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next
        
        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.value != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.value
        
        if not curr_1 or not curr_2:
            return
        
        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2
        
        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1
        
        curr_1.next, curr_2.next = curr_2.next, curr_1.next
    
    def reverse_itertative(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev
    
    @staticmethod
    def merge_2_sorted_LL(ll1, ll2):
        result = LinkedList()
        curr_1 = ll1.head
        curr_2 = ll2.head
        curr_res = result.head

        while curr_1 and curr_2:
            if curr_1.data > curr_2.data:
                result.append(curr_2.data)
                curr_2 = curr_2.next
            else:
                result.append(curr_1.data)
                curr_1 = curr_1.next
        
        while curr_1:
            result.append(curr_1.data)
            curr_1 = curr_1.next

        while curr_2:
            result.append(curr_2.data)
            curr_2 = curr_2.next
        
        return result
    
    def remove_dublicates(self):
        frq = dict()
        curr = self.head
        prev = None

        while curr:
            if frq.get(curr.data):
                prev.next = curr.next
            else:
                frq[curr.data] = 1
                prev = curr        
            curr = curr.next
    
    def get_nth_node(self, n):
        curr = self.head
        nth_from_curr = self.head
        while n and nth_from_curr:
            nth_from_curr = nth_from_curr.next
            n -= 1
        
        while nth_from_curr:
            curr = curr.next
            nth_from_curr = nth_from_curr.next

        if curr:
            return curr.data
        return None

    def rotate(self, k):
        end = self.head
        pivot = self.head

        while k>1 and pivot.next:
            k -= 1
            pivot = pivot.next
            end = end.next
        
        if pivot.next:
            while end.next:
                end = end.next
            end.next = self.head
            self.head = pivot.next
            pivot.next = None
    
    def move_tail_to_head(self):
        curr = self.head
        prev = None
        while curr.next:
            prev = curr
            curr = curr.next
        curr.next = self.head
        self.head = curr
        prev.next = None

    def sum_two_lists(self, llist):
        result = LinkedList()
        curr_1 = self.head
        curr_2 = llist.head
        
        carry_one = False
        while curr_1 and curr_2:
            res = curr_2.data + curr_1.data
            if carry_one:
                res += 1
            if res <= 9:
                carry_one = False
                result.append(res)
            else:
                result.append(res - 10)
                carry_one = True
            
            curr_1, curr_2 = curr_1.next, curr_2.next
        
        while curr_1:
            if carry_one:
                result.append(curr_1.data+1)
                carry_one = False
            else:
                result.append(curr_1.data)
            curr_1 = curr_1.next

        while curr_2:
            if carry_one:
                result.append(curr_2.data+1)
                carry_one = False
            else:
                result.append(curr_2.data)
            curr_2 = curr_2.next
        return result           
