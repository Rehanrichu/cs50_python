class Jar:
    def __init__(self, capacity=12):
        """
        Initialize a Jar with given capacity (maximum number of cookies).
        Raise ValueError if capacity is not a non-negative int.
        """
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("capacity must be a non-negative int")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        """Return a string of cookie emojis equal to the number of cookies."""
        return "🍪" * self._size

    def deposit(self, n):
        """
        Add n cookies to the jar.
        Raise ValueError if n is not a non-negative int or if it would exceed capacity.
        """
        if not isinstance(n, int) or n < 0:
            raise ValueError("deposit amount must be a non-negative int")
        if self._size + n > self._capacity:
            raise ValueError("deposit would exceed jar capacity")
        self._size += n

    def withdraw(self, n):
        """
        Remove n cookies from the jar.
        Raise ValueError if n is not a non-negative int or if there aren't enough cookies.
        """
        if not isinstance(n, int) or n < 0:
            raise ValueError("withdraw amount must be a non-negative int")
        if n > self._size:
            raise ValueError("not enough cookies to withdraw")
        self._size -= n

    @property
    def capacity(self):
        """Return the jar's capacity (read-only)."""
        return self._capacity

    @property
    def size(self):
        """Return the number of cookies in the jar."""
        return self._size
