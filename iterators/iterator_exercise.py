# Create a peeker class for an iterator

class Peeker(object):
    def __init__(self, inner_iter):
        self.inner_iter = inner_iter
        self.known_next_val = None
    
    def next(self):
        if self.known_next_val is None:
            return next(self.inner_iter)
        else: 
            next_val = self.known_next_val         
            self.known_next_val = None
            return next_val    

    def peek(self):
        # ...
        if self.known_next_val is None:
            self.known_next_val = next(self.inner_iter)
        return self.known_next_val


iterable_object = iter(["a", "b", "c", "d", "e", "f", "g"])

i = Peeker(iterable_object)

print(i.peek())
print(i.next())
print(i.peek())