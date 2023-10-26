class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        ...

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, n):
       if int(n) < 0:
           raise ValueError("Invalid capacity")
       self._capacity = int(n)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        if self._size >= self._capacity:
            raise ValueError("Not enough space")
        self._size += n


if __name__ == "__main__":

