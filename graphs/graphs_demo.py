class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return self.items == []

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.items[-1]

    def size(self):
        return len(self.items)

class HumanNode(object):

    def __init__(self, name, adjacent=None):
        if adjacent is None:
            adjacent = set()

        # isinstance() returns True if the specified object is of the 
        # specified type, otherwise False.
        assert isinstance(adjacent, set)
        # assert condition:
        # assert tests condition, and will trigger error if cond is false
        self.name = name
        self.adjacent = adjacent

class FriendGraph(object):
    # Undirected graphs: use two-element sets to represent them
    # Adjacencies be tracked via matrix or array  
    def __init__(self):

        self.nodes = set()

    def add_person(self, person):
        self.nodes.add(person)

    def set_friends(self, person1, person2):

        person1.adjacent.add(person2)
        person2.adjacent.add(person1)

    def are_connected(self, person1, person2):
        # BFS using queue
        possible_nodes = Queue()
        seen = set()
        possible_nodes.enqueue(person1)
        seen.add(person1)

        while not possible_nodes.is_empty():
            person = possible_nodes.dequeue()
            if person is person2:
                return True
            else:
                for friend in person.adjacent - seen:
                    possible_nodes.enqueue(friend)
                    seen.add(friend)
                    print("Added to queue: ", friend)
        return False

