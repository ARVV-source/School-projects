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

  def isEmpty(self):
    if self.head == None:
      return True
    else:
      return False
  
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

  def show(self):
    if self.isEmpty():
      return [None]
    else:
      line = []
      currentData = self.head
      while currentData.next != None:
        line.append(currentData.data)
        currentData = currentData.next
      line.append(currentData.data)
      return line
    
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

  def peek(self):
    return self.head.data
  
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


cola = Line()
cola.queue("hola")
cola.queue("mundo")
cola.queue("como")
cola.queue("estan")
print(cola.show())
print(cola.size())
print(cola.peek())
cola.Dequeue()
print(cola.show())