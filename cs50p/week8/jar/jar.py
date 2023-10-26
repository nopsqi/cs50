class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n

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
        if n > self._capacity:
            raise ValueError("Not enough space")
        if n < 0:
            raise ValueError("Not enough cookies")
        self._size = n


if __name__ == "__main__":
    jar = Jar(15)
    jar.deposit(5)
    jar.withdraw(2)
    print(jar)
