class Jar:
    def __init__(self, capacity=12):
        ...

    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, n):
       if int(n) < 0:
           raise ValueError
       self._capacity = int(n)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        


if __name__ == "__main__":

