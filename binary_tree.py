from queue import Queue
from stack import Stack


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def insert_BST(self, data):
        self.insert_helper(data, self.root)
    
    def insert_helper(self, data, node):
        if node:
            if data >= node.data:
                node.right = self.insert_helper(data, node.right)
            else:
                node.left = self.insert_helper(data, node.left)
            return node
        else:
            return Node(data)
    
    def search_BST(self, data):
        return self.search_helper(data, self.root)
    
    def search_helper(self, data, node):
        if node:
            if data == node.data:
                return node
            elif data < node.data:
                return self.search_helper(data, node.left)
            else:
                return self.search_helper(data, node.right)
    
    def preorder(self, node, traversal):
        if node:
            traversal += (str(node.data) + "-")
            traversal = self.preorder(node.left, traversal)
            traversal = self.preorder(node.right, traversal)
        return traversal
    
    def inorder(self, node, traversal):
        if node:
            traversal = self.inorder(node.left, traversal)
            traversal += (str(node.data) + "-")
            traversal = self.inorder(node.right, traversal)
        return traversal
    
    def postorder(self, node, traversal):
        if node:
            traversal = self.postorder(node.left, traversal)
            traversal = self.postorder(node.right, traversal)
            traversal += (str(node.data) + "-")
        return traversal
    
    def levelorder(self, node, traversal):
        queue = Queue()
        queue.enqueue(node)

        while not queue.is_empty():
            curr = queue.dequeue()
            if not curr:
                continue
            traversal += (str(curr.data) + "-")
            queue.enqueue(curr.left)
            queue.enqueue(curr.right)
        return traversal
    
    def reverselevelorder(self, node, traversal):
        stack = Stack()
        queue = Queue()
        queue.enqueue(node)

        while not queue.is_empty():
            curr = queue.dequeue()
            if not curr:
                continue
            stack.push(curr)
            queue.enqueue(curr.right)
            queue.enqueue(curr.left)
        
        while not stack.is_empty():
            traversal +=  str(stack.pop().data) +"-"
        
        return traversal

    def traverse(self, order):
        order_dict = {
            "pre": self.preorder,
            "in": self.inorder,
            "post": self.postorder,
            "lvl": self.levelorder,
            "reverse": self.reverselevelorder
            }
        return order_dict[order](self.root, "")[:-1] if order in order_dict else None 
    
    def height(self, node):
        if node is None:
            return -1
        
        left_height = self.height(self.left)
        right_height = self.height(self.right)

        return 1 + max(left_height, right_height)
    
    def length(self, node):
      if node is None:
        return 0 

      return 1 + self.length(node.left) + self.length(node.right)
    
    def __len__(self):
        return self.length(self, self.root)
