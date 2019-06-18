from abc import ABC, abstractmethod
import random

# Base class for constraints
class Constraint(ABC):
    """
    Abstract base class for a 'constraint' in the context of 
    constraint-satisfaction problems.

    Contains a list of variables on which the constraint is applied, and an
    abstract method satisfied() to test whether constraint is met.
    """
    def __init__(self, variables):
        self.variables = variables

    @abstractmethod
    def satisfied(self, assignment):
        raise NotImplementedError

class ConstraintSatisfactionProblem(object):
    """
    Class for setting up and solving a generic constraint satisfaction problem.

    Requires a list of *variables* and a dictionary *domains* that maps each
    variable to a list of domains.
    """
    def __init__(self, variables, domains, verbose=False, relaunch=1e6):
        self.variables = variables
        self.domains = domains
        self.verbose = verbose
        self.relaunch = relaunch
        self._call_count = 0

        # Initialize constraints
        self.constraints = {}
        for var in self.variables:
            # Make sure problem is set up appropriately
            if var not in self.domains:
                raise LookupError(("Every variable must have at least one ",
                                   "domain assigned to it"))
            self.constraints[var] = []

    def add_constraint(self, constraint):
        """
        Add a constraint to the variables listed in the CSP.
        """
        for var in constraint.variables:
            if var not in self.variables:
                raise LookupError("{} not found in variables".format(var))
            else:
                self.constraints[var].append(constraint)

    def consistent(self, variable, assignment):
        """
        Check if given assignment is consistent with all constraints on
        given variable.
        """
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtracking_search(self, assignment={}):
        """
        Recursive search through variables to ensure all variables are
        assigned with all constraints met.
        """
        self._call_count += 1
        if self.verbose:
            print("Call # {} to backtracking search".format(self._call_count))
        # If the church has gon
        if self._call_count > self.relaunch:
            assignment = {}
            random.shuffle(self.variables)
            self._call_count = 0
        # Base-case of recursion: all variables successfully assigned
        if len(assignment) == len(self.variables):
            return assignment

        # Get all variables from the problem that are not in the assignment
        unassigned = [v for v in self.variables if v not in assignment]

        # Get all possible domain values of the first unassigned variable
        first = unassigned[0]
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            if self.consistent(first, local_assignment):
                result = self.backtracking_search(local_assignment)
                if result is not None:
                    return result
        return None
