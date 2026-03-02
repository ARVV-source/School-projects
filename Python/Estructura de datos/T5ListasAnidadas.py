class Node:
  def __init__ (self, data):
    self.data = data
    self.next = None

  def setNext(self, nextNode: 'Node'):
    self.next = nextNode

  def getNext(self):
    return self.next
  
  def setData(self, newData):
    self.data = newData
  
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

  def removeValue(self, removedValue):
    if self.isEmpty():
      return
    else:
      current = self.head
      while current.next.data != removedValue:
        current = current.next
      removedNode = current.next
      current.setNext(removedNode.next)
  
  def removePosition(self, removedIndex):
    if removedIndex > (self.size()-1):
      return
    elif 0 > removedIndex:
      return 
    elif 0 == removedIndex:
      self.head = self.head.next
    else:
      current = self.head
      for i in range(removedIndex-1):
        current = current.next
      current.setNext(current.next.next)

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
    
#____________________________________ Aqui empiezan ________________________________________

  def addSort(self, newData):
    self.add(newData)
    self.sort()
  
  def sort(self):
    if self.head == None:
      return
    current = self.head
    while current != None:
      comparison = current.next
      while comparison != None:
        if comparison.data < current.data:
          current.data, comparison.data = comparison.data, current.data
        comparison = comparison.next
      current = current.next

  def seek(self, wantedValue):
    if self.isEmpty():
      return -1
    start = self.head
    end = None
    while start != end:
      slow = start
      fast = start
      while fast != end and fast.next != end:
        fast = fast.next.next
        slow = slow.next
      if slow.data == wantedValue:
        index = 0
        current = self.head
        while current != slow:
          index += 1
          current = current.next
        return index
      elif slow.data < wantedValue:
        start = slow.next
      else:
        end = slow
    return -1