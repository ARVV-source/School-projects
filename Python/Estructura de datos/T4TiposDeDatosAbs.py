#_____________________________________________________________#
class Node:
  def __init__ (self, data):
    self.data = data
    self.next = None

  def setNext(self, nextNode):
    self.next = nextNode

  def getNext(self):
    return self.next

class Line:
  head = None
  tail = None

  def queue(self, newData):
    nextQueue = Node(newData)
    if self.isEmpty():
      self.head = nextQueue
      self.tail = nextQueue
    else:
      self.tail.setNext(nextQueue)
      self.tail = nextQueue

  def Dequeue(self):
    if self.isEmpty():
      return None
    else:
      outgoingNode = self.head
      self.head = self.head.next
      return outgoingNode.data
  
  def peek(self):
    return self.head.data

  def size(self):
    if self.isEmpty():
      return 0
    else:
      size=0
      currentData = self.head
      while currentData.next != None:
        size += 1
        currentData = currentData.next
      size += 1
      return size
    
  def show(self):
    if self.isEmpty():
      return None
    else:
      line = []
      currentData = self.head
      while currentData.next != None:
        line.append(currentData.data)
        currentData = currentData.next
      line.append(currentData.data)
      return line
    
  def isEmpty(self):
    if self.head == None:
      return True
    else:
      return False
    
  def find(self, peekabo):
    list = self.show()
    index = 0
    for current in list:
      if current == peekabo:
        return index
      else:
        index += 1
        pass
    return -1
    
#_____________________________________________________________#

class Stack:
  top = None

  def push(self, newData):
    newTop = Node(newData)
    newTop.setNext(self.top)
    self.top = newTop
    
  def pop(self):
    self.top = self.top.next
    return self.top
  
  def peek(self):
    return self.top
  
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
        print(current.data ,end=" ")
        current = current.next
      print()

  def isEmpty(self):
    if self.top == None:
      True
    else:
      False

pila = Stack()
pila.push(10)
pila.push(20)
pila.push(30)
pila.show()
pila.pop()
pila.show()
