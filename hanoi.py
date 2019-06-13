"""
Towers of Hanoi
"""

class Stack(list):
    """
    A stack derived from the python list.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '\n'.join(str(val) for val in self)

    def push(self, item):
        self.append(item)

def solve(begin, end, intermediary, disc):
    """
    Recursive solution to Towers of Hanoi.

    Parameters
    ----------
    begin :        Stack
        Initial tower on which the discs are located.
    end   :        Stack
        Empty tower to which the discs are to be transported
    intermediary : Stack
        Empty tower to be used as intermediary for disc transfer
    disc :         int
        Disc number
    """
    print(begin, intermediary, end, '\n')
    if disc == 1:
        end.push(begin.pop())
    else:
        solve(begin, intermediary, end, disc - 1)
        solve(begin, end, intermediary, 1)
        solve(intermediary, end, begin, disc - 1)
