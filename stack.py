class Stack:
    def __init__(self):
        self.array = []
    
    def pop(self):
        try:
            return self.array.pop()
        except:
            return None
    
    def peak(self):
        if len(self.array):
            return self.array[-1]
    
    def push(self, elem):
        self.array.append(elem)
    
    def is_empty(self):
        return False if len(self.array) else True


def is_balanced(s): 
    stack = Stack()
    for char in s:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            opening = stack.pop()
            if not (opening and opening+char in "(){}[]"):
                return False
    return True if stack.is_empty() else False

def reverse_str(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    output = ""
    while(not stack.is_empty()):
        output += stack.pop()
    return output

def convert_int_to_bin(dec_num):
  stack = Stack()
  output = ""
  while dec_num > 0 :
    stack.push(dec_num%2)
    dec_num =int(dec_num/2)
  while not stack.is_empty():
    output += str(stack.pop())
  return output
