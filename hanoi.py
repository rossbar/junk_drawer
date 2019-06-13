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

class TowersOfHanoi(object):
    """
    Towers of Hanoi
    """
    def __init__(self, num_discs=3):
        self.tower_1 = Stack()
        self.tower_2 = Stack()
        self.tower_3 = Stack()
        self.num_discs = num_discs
        # Initialize tower
        for disc in range(1, self.num_discs + 1):
            self.tower_1.push(disc)
        # Counter for number of recursive calls needed to solve
        self._num_steps = 0

    def __repr__(self):
        out = ''
        for i in range(self.num_discs):
            for tower in self.towers:
                if len(tower) <= i:
                    out += "|"
                else:
                    out += str(tower[i])
                out += "\t"
            out += "\n"
        return out

    @property
    def towers(self):
        return (self.tower_1, self.tower_2, self.tower_3)

    def _step(self, begin, end, temp, disc, verbose=True):
        """
        Recursive solution to towers of Hanoi.

        If verbose is True, print out state of towers at every step
        """
        if disc == 1:
            end.push(begin.pop())
        else:
            self._step(begin, temp, end, disc - 1)
            self._step(begin, end, temp, 1)
            self._step(temp, end, begin, disc - 1)
        self._num_steps += 1
        if verbose:
            print("Step %i:" %(self._num_steps))
            print(self)

    def solve(self, verbose=True):
        """
        Kick-off recursive solution chain.
        """
        self._step(self.tower_1, self.tower_3, self.tower_2, self.num_discs,
                   verbose=verbose)

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
    if disc == 1:
        end.push(begin.pop())
    else:
        solve(begin, intermediary, end, disc - 1)
        solve(begin, end, intermediary, 1)
        solve(intermediary, end, begin, disc - 1)
