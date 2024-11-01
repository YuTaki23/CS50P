class Jar:
    def __init__(self, capacity=12):
        if (capacity <= 0):
            raise ValueError("Invalid capacity.")
        self._capacity = capacity
        self.jar_size = 0

    def __str__(self):
        return "🍪" * self.jar_size

    def deposit(self, n):
        if (self.jar_size + n > self._capacity):
            raise ValueError("More than capacity.")
        self.jar_size += n

    def withdraw(self, n):
        if (self.size < n):
            raise ValueError("There are not enough jars.")
        self.jar_size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.jar_size        
