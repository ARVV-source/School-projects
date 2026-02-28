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
    size=0
    if self.isEmpty():
      return size
    else:
      currentData = self.head
      while currentData != None:
        size += 1
        currentData = currentData.next
      return size
    
  def show(self):
    if self.isEmpty():
      return None
    else:
      current = self.head
      while current != None:
        print(current.data, end=" ")
        current = current.next
      print()
    
  def isEmpty(self):
    if self.head == None:
      return True
    else:
      return False
    
  def find(self, peekabo):
    index = 0
    if self.isEmpty():
      return -1
    else:
      current = self.head
      while current != None:
        if current.data == peekabo:
          return index
        else:
          index += 1
          current = current.next
          pass
      return -1

#print("Colas")
#line = Line()
#line.queue("hola")
#line.queue("mundo")
#line.queue("Python")
#print(line.Dequeue())
#print(line.peek())
#print(line.size())
#line.show()
#print(line.isEmpty())
#print(line.find("Python"))
#print(line.find("Java"))

#_____________________________________________________________#

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
        print(current.data ,end=" ")
        current = current.next
      print()

  def isEmpty(self):
    if self.top == None:
      return True
    else:
      return False

#print("Pilas")
#stack = Stack()
#stack.push("silla 1")
#stack.push("silla 2")
#stack.push("silla 3")
#print(stack.pop())
#print(stack.peek())
#print(stack.size())
#stack.show()
#print(stack.isEmpty())

#_____________________________________________________________#

class List:
  head = None
  tail = None

  def add(self, newData):
    nextQueue = Node(newData)
    if self.isEmpty():
      self.head = nextQueue
      self.tail = nextQueue
    else:
      self.tail.setNext(nextQueue)
      self.tail = nextQueue

  def insertAt(self, newData, desireIndex):
    newNode = Node(newData)
    if desireIndex > self.size():
      return
    elif 0 > desireIndex:
      return 
    elif 0 == desireIndex:
      newNode.setNext(self.head)
      self.head = newNode
    else:
      current = self.head
      for i in range(desireIndex-1):
        current = current.next
      newNode.setNext(current.next)
      current.setNext(newNode)

  def size(self):
    size=0
    if self.isEmpty():
      return size
    else:
      currentData = self.head
      while currentData != None:
        size += 1
        currentData = currentData.next
      return size
    
  def show(self):
    if self.isEmpty():
      return None
    else:
      current = self.head
      while current != None:
        print(current.data, end=" ")
        current = current.next
      print()

  def isEmpty(self):
    if self.head == None:
      return True
    else:
      return False
    
lst = List()
lst.add(1)
lst.add(2)
lst.add(4)
lst.show()
lst.insertAt(3, 2)
lst.show()