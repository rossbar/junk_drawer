"""
Example using constraint-satisfaction framework to solve the map-coloring
problem.
"""
from constraint_satisfaction import Constraint

class MapColorConstraint(Constraint):
    """
    Binary constraint for map coloring problem.
    """
    def __init__(self, place_1, place_2):
        super().__init__([place_1, place_2])
        self.place_1 = place_1
        self.place_2 = place_2

    def satisfied(self, assignment):
        """
        Map color constraint is satisfied if either place's color hasn't
        been assigned, or they are not the same.
        """
        if self.place_1 not in assignment or self.place_2 not in assignment:
            return True
        return assignment[self.place_1] != assignment[self.place_2]

# Specification of map-coloring problem for Australia
australia = {
    "variables"   : ["Western Australia", "Northern Territory", 
                     "South Australia", "Queensland", "New South Wales",
                     "Victoria", "Tasmania"],
    "domain"     : ["red", "green", "blue"],
    "constraints" : [MapColorConstraint("Western Australia", "Northern Territory"),
                     MapColorConstraint("Western Australia", "South Australia"),
                     MapColorConstraint("South Australia", "Northern Territory"),
                     MapColorConstraint("Queensland", "Northern Territory"),
                     MapColorConstraint("Queensland", "South Australia"),
                     MapColorConstraint("Queensland", "New South Wales"),
                     MapColorConstraint("New South Wales", "South Australia"),
                     MapColorConstraint("Victoria", "South Australia"),
                     MapColorConstraint("Victoria", "New South Wales"),
                     MapColorConstraint("Victoria", "Tasmania")]
}

if __name__ == "__main__":
    from constraint_satisfaction import ConstraintSatisfactionProblem as CSP
    # Construct domain for each variable
    domains = { v : australia["domain"] for v in australia["variables"] }
    # Initialize CSP framework
    map_coloring_problem = CSP(australia["variables"], domains)
    # Add constraints
    for c in australia["constraints"]:
        map_coloring_problem.add_constraint(c)

    # Solve problem
    solution = map_coloring_problem.backtracking_search()
    if solution is None:
        print("Failed to find solution")
    else:
        print(solution)
