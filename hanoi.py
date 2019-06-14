"""
Towers of Hanoi
"""
from data_structures import Stack

class TowersOfHanoi(object):
    """
    Towers of Hanoi
    """
    def __init__(self, num_discs=3, verbose=True):
        self.tower_1 = Stack()
        self.tower_2 = Stack()
        self.tower_3 = Stack()
        self.num_discs = num_discs
        self.verbose = verbose
        # Initialize tower
        for disc in range(self.num_discs, 0, -1):
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
        # Flip UD
        return "\n".join(out.split("\n")[::-1])

    @property
    def towers(self):
        return (self.tower_1, self.tower_2, self.tower_3)

    def _step(self, begin, end, temp, disc):
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
        if self.verbose:
            print("Step %i:" %(self._num_steps))
            print(self)

    def solve(self):
        """
        Kick-off recursive solution chain.
        """
        self._step(self.tower_1, self.tower_3, self.tower_2, self.num_discs)

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

def classic_solution():
    """
    Create an instance of the classic Towers of Hanoi problem and solve it
    verbosely.
    """
    towers = TowersOfHanoi()
    towers.solve()

def evaluate_performance(disc_max=21):
    """
    Evaluate how the recursive solution to the Towers of Hanoi problem scales
    with the number of discs.
    """
    print("Computing Solution for up to {} discs...".format(disc_max - 1))
    import matplotlib.pyplot as plt
    from timeit import timeit

    # Set up plot
    fig, ax = plt.subplots()
    ax2 = ax.twinx()
    ax.set_title("Performance of Recursive Solution to Towers of Hanoi")
    ax.set_xlabel("Number of Discs")
    ax.set_ylabel("Evaluation time (s)")
    ax2.set_ylabel("# Recursive function calls")

    disc_range = range(3, disc_max)
    eval_times, num_calls = [], []
    for num_discs in disc_range:
        towers = TowersOfHanoi(num_discs, verbose=False)
        eval_times.append(timeit(towers.solve, number=1))
        num_calls.append(towers._num_steps)

    ax.plot(disc_range, eval_times)
    ax2.plot(disc_range, num_calls)
    fig.tight_layout()
    plt.show()

if __name__ == "__main__":
    classic_solution()
    evaluate_performance()
