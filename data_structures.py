"""
Some data structures not included in collections
"""

class Stack(list):
    """
    A stack derived from the python list.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '\n'.join(str(val) for val in self)

    @property
    def empty(self):
        return len(self) == 0

    def push(self, item):
        self.append(item)
