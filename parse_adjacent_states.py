"""
Script to parse a webpage containing data on which states are adjacent to
one another into a json file.

Useful for generating data for a more involved test of the map_coloring
problem.
"""
import requests
import json
from bs4 import BeautifulSoup

# Website with desired information in a table
url = "https://thefactfile.org/u-s-states-and-their-border-states/"
r = requests.get(url)
soup = BeautifulSoup(r.text)

# Get HTML tags corresponding to relevant data columns (N.B. - specific to data
# format of site)
state_tags = soup.find_all('td', attrs={'class':"column-2"})
adj_state_tags = soup.find_all('td', attrs={'class':"column-3"})

# Create lists of relevant data
states = [state.contents[0] for state in state_tags]
adj_states = [row.contents[0].split(',') for row in adj_state_tags]

# Clean up the data on adjacent states from the site
for i, sl in enumerate(adj_states):
    for j, s in enumerate(sl):
        s = s.replace("(water border)", "")
        adj_states[i][j] = s.strip()
        
# Remap the 'adjacent states' data back onto the corresponding state
adj_states_dict = { s : asl for (s, asl) in zip(states, adj_states) }

# Save the results
with open("data/adjacent_states.json", "w") as fh:
    json.dump(adj_states_dict, fh)
