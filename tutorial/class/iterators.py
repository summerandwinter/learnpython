class Reverse:
    """Iterator for looping over a sequence backwords."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    """Returns an object with ``__next__`` method .
    If the class defines ``__next__`` method,  then ``__iter__`` can just return ``self`` 
    """
    def __iter__(self):  #
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


if __name__ == '__main__':
    rev = Reverse("spam")
    print(iter(rev)) 
    for char in rev:
        print(char)

