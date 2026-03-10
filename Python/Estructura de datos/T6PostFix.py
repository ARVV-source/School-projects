class Node:
  def __init__ (self, data):
    self.data = data
    self.next = None

  def setNext(self, nextNode: 'Node'):
    self.next = nextNode

  def getNext(self):
    return self.next


class Stack:
  top = None

  def push(self, newData):
    newTop = Node(newData)
    newTop.setNext(self.top)
    self.top = newTop
    
  def pop(self):
    lastTop = self.top
    self.top = self.top.next
    return lastTop.data
  
  def peek(self):
    return self.top.data
  
  def size(self):
    if self.isEmpty():
      return 0
    else:
      current = self.top
      size = 0
      while current != None:
        size += 1
        current = current.next
      return size 
  
  def show(self):
    if self.isEmpty():
      return None
    else:
      current = self.top
      while current != None:
        print(current.data, end=" ")
        current = current.next
      print()

  def isEmpty(self):
    if self.top == None:
      return True
    else:
      return False


class PostFix:
  def evalPostFix(self, expresion):
    myStack = Stack()
    for i in expresion:
      if i in ["+", "-", "/", "*"]:
        b = myStack.pop()
        a = myStack.pop()
        match i:
          case "+":
            newNum = a + b
            myStack.push(newNum)
          case "-":
            newNum = a - b
            myStack.push(newNum)
          case "/":
            newNum = a / b
            myStack.push(newNum)
          case "*":
            newNum = a * b
            myStack.push(newNum)
          
      else:
        myStack.push(int(i))
    return myStack.pop()

postfix = PostFix()
print(postfix.evalPostFix("352*+73*-"))