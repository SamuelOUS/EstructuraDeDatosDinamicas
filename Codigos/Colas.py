class ErrorFull(Exception):
    pass


class ErrorEmpty(Exception):
    pass


class Queue:
    contQue = 0
    contMulti = 1
    cont = 0

    def __init__(self):
        self.length: int = 3
        self.queue: list = [None] * self.length

    def enqueue(self, e):

        if Queue.contQue < self.length:
            self.queue[Queue.contQue] = e
            Queue.contQue += 1

        else:

            for i in range(self.length):
                self.queue.append(None)

            self.length = self.length * 2

            self.queue[Queue.contQue] = e
            Queue.contQue += 1

    def dequeue(self):

        if queue_1.is_empty():
            raise ErrorEmpty("Empty queue")

        else:
            first = self.queue[0]
            self.queue.append(None)
            self.queue.pop(0)
            Queue.contQue -= 1
            return first

    def front(self):
        return self.queue[0]

    def is_empty(self):
        if Queue.contQue == 0:
            return True
        else:
            return False


queue_1 = Queue()

queue_1.dequeue()

print(len(queue_1.queue))
print(queue_1.queue)
print(queue_1.length)
