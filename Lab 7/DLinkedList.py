class DLinkedListNode:
    # An instance of this class represents a node in Doubly-Linked List
    def __init__(self,initData,initNext,initPrevious):
        self.data = initData
        self.next = initNext
        self.previous = initPrevious
        
        if initNext != None:
            self.next.previous = self
        if initPrevious != None:
            self.previous.next = self
            
    def getData(self):
        return self.data
    
    def setData(self,newData):
        self.data = newData
        
    def getNext(self):
        return self.next
    
    def getPrevious(self):
        return self.previous
    
    def setNext(self,newNext):
        self.next = newNext
        
    def setPrevious(self,newPrevious):
        self.previous = newPrevious


class DLinkedList:
    # An instance of this class represents the Doubly-Linked List
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0        
           
    def search(self, item):
        current = self.__head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
        return found
        
    def index(self, item):
        current = self.__head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
                index = -1
        return index        
         
    def add(self, item):
        NewNode = DLinkedListNode(item, self.__head, None)
        self.__head = NewNode
        Tail = None
        for i in range (0, self.getSize()):
            Tail = NewNode.getNext()
        if (Tail == None):
            self.__tail = NewNode
        else:
            self.__tail = Tail
        self.__size += 1
        
    def remove(self, item):
        Current = self.__head
        Found = False
        while Current != None and not Found:
            if (Current.getData() == item):
                Previous = Current.getPrevious()
                Next = Current.getNext()
                if (Previous != None):
                    Previous.setNext(Next)
                if (Next != None):
                    Next.setPrevious(Previous)
                self.__size -= 1
                Found = True
            Current = Current.getNext()
        
    def append(self, item):
        NewNode = DLinkedListNode(item, None, self.__tail)
        self.__tail = NewNode
        self.__size += 1

    def insert(self, pos, item):
        assert isinstance(pos, int), "Can't use a non-integer as position"
        assert pos >= 0, "Can't use a negative integer as position"
        if (pos == 0):
            self.add(item)
        elif (pos == self.getSize() - 1):
            self.append(item)
        else:
            Current = self.__head
            Inserted = False
            while not Inserted:
                if (self.index(Current.getData()) == pos - 1):
                    Previous = Current
                    Next = Current.getNext()
                    NewNode = DLinkedListNode(item, Next, Previous)
                    Previous.setNext(NewNode)
                    Next.setPrevious(NewNode)
                    self.__size += 1
                    Inserted = True
                Current = Current.getNext()
        
    def pop1(self):
        Tail = self.__tail
        Previous = Tail.getPrevious()
        if (Previous != None):
            Previous.setNext(None)
        self.__tail = Previous
        self.__size -= 1
        return Tail.getData()
    
    def pop(self, pos=None):
        if (pos == None):
            self.pop1()
        elif (pos >= self.getSize()):
            raise Exception("Position outside the list.")
        else:
            assert isinstance(pos, int), "Can't use a non-integer as position"
            assert pos >= 0, "Can't use a negative integer as position"
            Current = self.__head
            Popped = False
            Item = None
            while not Popped:
                if (self.index(Current.getData()) == pos):
                    Item = Current.getData()
                    Previous = Current.getPrevious()
                    Next = Current.getNext()
                    if (Previous != None):
                        Previous.setNext(Next)
                    if (Next != None):
                        Next.setPrevious(Previous)
                    if (Current == self.__head):
                        self.__head = Current.getNext()
                    if (Current == self.__tail):
                        self.__tail = Current.getPrevious()
                    self.__size -= 1
                    Popped = True
                Current = Current.getNext()
            print(Item)
            return Item
        
    def searchLarger(self, item):
        Position = -1
        Current = self.__head
        Found = False
        while Current != None and not Found:
            if (Current.getData() > item):
                Position = self.index(Current.getData())
                Found = True
            Current = Current.getNext()
        return Position
        
    def getSize(self):
        return self.__size
    
    def getItem(self, pos):
        assert isinstance(pos, int), "Can't use a non-integer as position"
        if (pos >= self.getSize()):
            raise Exception("Position outside the list.")
        elif (pos == 0):
            return self.__head.getData()
        elif (pos == self.getSize() - 1):
            return self.__tail.getData()
        elif (pos > 0):
            Current = self.__head
            Found = False
            Item = None
            while not Found:
                if (self.index(Current.getData()) == pos):
                    Item = Current.getData()
                    Found = True
                Current = Current.getNext()
            return Item
        elif (pos < 0):
            Current = self.__tail
            Found = False
            Item = None
            while not Found:
                if ((self.index(Current.getData() - self.getSize()) == pos)):
                    Item = Current.getData()
                    Found = True
                Current = Current.getPrevious()
            return Item
        
    def __str__(self):
        Current = self.__head
        StrRep = ""
        while Current != None:
            StrRep += f"{Current.getData()} "
            Current = Current.getNext()
        return StrRep.strip()


def test():
                  
    linked_list = DLinkedList()
                    
    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test"
            
    linked_list.add("World")
    linked_list.add("Hello")    
        
    is_pass = (str(linked_list) == "Hello World")
    assert is_pass == True, "fail the test"
              
    is_pass = (linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.getItem(0) == "Hello")
    assert is_pass == True, "fail the test"
        
        
    is_pass = (linked_list.getItem(1) == "World")
    assert is_pass == True, "fail the test"    
            
    is_pass = (linked_list.getItem(0) == "Hello" and linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.pop(1) == "World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.pop() == "Hello")
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test" 
                    
    int_list2 = DLinkedList()
                    
    for i in range(0, 10):
        int_list2.add(i)      
    int_list2.remove(1)
    int_list2.remove(3)
    int_list2.remove(2)
    int_list2.remove(0)
    is_pass = (str(int_list2) == "9 8 7 6 5 4")
    assert is_pass == True, "fail the test"
                
    for i in range(11, 13):
        int_list2.append(i)
    is_pass = (str(int_list2) == "9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    for i in range(21, 23):
        int_list2.insert(0,i)
    is_pass = (str(int_list2) == "22 21 9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    is_pass = (int_list2.getSize() == 10)
    assert is_pass == True, "fail the test"
                    
    int_list = DLinkedList()
                    
    is_pass = (int_list.getSize() == 0)
    assert is_pass == True, "fail the test"                   
                    
    for i in range(0, 1000):
        int_list.append(i)
    correctOrder = True
            
    is_pass = (int_list.getSize() == 1000)
    assert is_pass == True, "fail the test"            
            
        
    for i in range(0, 200):
        if int_list.pop() != 999 - i:
            correctOrder = False
                            
    is_pass = correctOrder
    assert is_pass == True, "fail the test" 
            
    is_pass = (int_list.searchLarger(200) == 201)
    assert is_pass == True, "fail the test" 
            
    int_list.insert(7,801)   
        
    is_pass = (int_list.searchLarger(800) == 7)
    assert is_pass == True, "fail the test"
            
            
    is_pass = (int_list.getItem(-1) == 799)
    assert is_pass == True, "fail the test"
            
    is_pass = (int_list.getItem(-4) == 796)
    assert is_pass == True, "fail the test"
                    
    if is_pass == True:
        print ("=========== Congratulations! Your have finished exercise 2! ============")

                
if __name__ == '__main__':
    test()
