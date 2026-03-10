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
    expresion = self.split(expresion)
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
  
  def split(self, expresion, number = "", newExpresion = []):
    for i in expresion:
      if i in ["1","2","3","4","5","6","7","8","9"]:
        number = number+i

      elif i == " ":
        if number == "":
          pass
        else:
          newExpresion.append(number)
          number = ""

      elif i in ["+", "-", "/", "*"]:
        newExpresion.append(i)
    return newExpresion


postfix = PostFix()
print(postfix.evalPostFix("5 6 2 + * 12 4 / -"))
