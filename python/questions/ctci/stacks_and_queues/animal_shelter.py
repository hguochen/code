"""
CtCi
3.6 An animal shelter, which holds only dogs and cats, operates on a strictly
"first in, first out" basis. People must adopt either the "oldest"(based on arrival time)
of all animals at the shelter, or they can select whether they would prefer a dog or
a cat(and will receive the oldest animal of that type). They cannot select which
specific animal they would like. Create the data structures to maintain this system
and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You
may use the built in LinkedList data structure.
"""

class AnimalShelter(object):
    def __init__(self):
        self.shelter = []
        self.temp = []

    def enqueue(self, animal):
        self.shelter.append(animal)

    def dequeue_any(self):
        if len(self.shelter) < 1:
            return None
        return self.shelter.pop(0)

    def dequeue(self, animal):
        if len(self.shelter) < 1:
            return None
        while self.shelter[0] != animal:
            self.temp.append(self.shelter.pop(0))
            if len(self.shelter) < 1:
                return None
        result = self.shelter.pop(0)
        while len(self.temp) > 0:
            self.shelter.insert(0, self.temp.pop())
        return result

    def print_shelter(self):
        print self.shelter
        
if __name__ == '__main__':
    shelter = AnimalShelter()
    shelter.enqueue('C')
    shelter.enqueue('C')
    shelter.enqueue('D')
    shelter.enqueue('C')
    shelter.enqueue('D')
    # print shelter.dequeue_any()
    # print shelter.dequeue_any()
    # print shelter.dequeue_any()
    # print shelter.dequeue_any()
    print shelter.dequeue('D')
    shelter.print_shelter()
    print shelter.dequeue('D')
    shelter.print_shelter()