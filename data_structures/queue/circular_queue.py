class CircularQueue:

    #Constructor
    def __init__(self):
        self.queue = list()
        self.head = 0
        self.tail = 0
        self.max_size = 8

    #Adding elements to the queue
    def enqueue(self,data):
        """
        Insert the element in the Queue
        >>> CQ=CircularQueue()
        >>> CQ.enqueue(5)
        True
        >>> CQ.size()
        1
        """
        if self.size() == self.max_size-1:
            return ("Queue Full!")
        self.queue.append(data)
        self.tail = (self.tail + 1) % self.max_size
        return True

    #Removing elements from the queue
    def dequeue(self):
        """
        Delete the element from the Queue
        >>> CQ=CircularQueue()
        >>> CQ.enqueue(5)
        True
        >>> CQ.dequeue()
        5
        >>> CQ.size()
        0
        """
        if self.size()==0:
            return ("Queue Empty!")
        data = self.queue[self.head]
        self.head = (self.head + 1) % self.max_size
        return data

    #Calculating the size of the queue
    def size(self):
        """
        >>> CQ=CircularQueue()
        >>> CQ.enqueue(5)
        True
        >>> CQ.size()
        1
        """
        if self.tail>=self.head:
            return (self.tail-self.head)
        return (self.max_size - (self.head-self.tail))

q = CircularQueue()

for i in range(10):
    print(q.enqueue(i))

while q.size():
    print(q.dequeue())
