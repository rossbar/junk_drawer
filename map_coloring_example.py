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

def setup_australia():
    """
    Set up map color problem for australia
    """
    # Construct domain for each variable
    domains = { v : australia["domain"] for v in australia["variables"] }
    return australia['variables'], domains, australia['constraints']

def setup_america():
    """
    Set up of the problem for America.
    """
    import json
    # Load data
    with open('data/adjacent_states.json', 'r') as fh:
        adj_states_dict = json.load(fh)
    # Set up variables
    variables = list(adj_states_dict.keys())
    # Set up domains
    domain = ['red', 'green', 'blue', 'yellow']
    domains = { v : domain for v in variables }
    # Set up constraints
    constraints = []
    for state in variables:
        for border in adj_states_dict[state]:
            if border != 'None' and len(border) > 0:
                constraints.append(MapColorConstraint(state, border))
    return variables, domains, constraints

def plot_america_result(state_color_dict):
    """
    Given the assignment returned by a successful constraint-satisfaction
    solution of the map-coloring problem for the US states, produce an
    MPL-based plot to visualize the result.

    Based on answer to this stack overflow post:
    https://stackoverflow.com/questions/53290602/how-to-use-cartopy-to-create-colored-us-states
    """
    import matplotlib.pyplot as plt
    import cartopy.crs as ccrs
    from cartopy.io import shapereader

    # Set up figure for displaying US map
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1], projection=ccrs.LambertConformal())
    ax.set_extent([-125, -66.5, 20, 50], ccrs.Geodetic())

    # Get natural earth data for US states
    # (see https://scitools.org.uk/cartopy/docs/v0.15/tutorials/using_the_shapereader.html)
    shapename = 'admin_1_states_provinces_lakes_shp'
    states_shp = shapereader.natural_earth(resolution='110m',
                                           category='cultural',
                                           name=shapename)

    # Set up axes for display
    ax.background_patch.set_visible(False)
    ax.outline_patch.set_visible(False)
    ax.set_title("Solution to Map Coloring Problem: US States")
    
    # Colorize the states
    for state in shapereader.Reader(states_shp).records():
        try:
            ax.add_geometries([state.geometry], ccrs.PlateCarree(),
                              facecolor=state_color_dict[state.attributes['name']],
                              edgecolor='black')
        except KeyError:
            pass
    plt.show()
    return fig


if __name__ == "__main__":
    from constraint_satisfaction import ConstraintSatisfactionProblem as CSP
    # Load data
    variables, domains, constraints = setup_america()
    # Initialize CSP framework
    map_coloring_problem = CSP(variables, domains, verbose=True)
    # Add constraints
    for c in constraints:
        map_coloring_problem.add_constraint(c)

    # Solve problem
    solution = map_coloring_problem.backtracking_search()
    if solution is None:
        print("Failed to find solution")
    else:
        #print(solution)
        plot_america_result(solution)
        print("Number of calls to backtracking search: {}".format(map_coloring_problem._call_count))
