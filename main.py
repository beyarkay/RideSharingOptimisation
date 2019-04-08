import math
import typing

"""
Objects:
Driver
    * Schedule
Child
    * Schedule
location_ids
    * loc 1
    * loc 2
    * loc 3 ...
"""
IN_TRANSIT = "IN_TRANSIT"
TIME_STEPS = 1000
locations = ["IN_TRANSIT",
             "Home A",
             "Home B",
             "School",
             "Rugby",
             "Hockey"]
# distances[a][b] = time from a to b
""" 
Template For Building the Distances Matrix
    note: often easier to use the grid builder
distances = [[-1, -1, -1, -1, -1, -1],
             [-1, -1, __, __, __, __],
             [-1, __, -1, __, __, __],
             [-1, __, __, -1, __, __],
             [-1, __, __, __, -1, __],
             [-1, __, __, __, __, -1]]
"""


def get_distances_matrix(verbose=False):
    distances = [[-1 for _j in locations] for _i in locations]

# Get the user entered locations
    coords = []
    for i, location in enumerate(locations[1:]):
        # Intermediate variables
        question = "Coordinates of {}({}) as _x_ _y_: ".format(location, i)
        plekke = (input(question)).split(" ")
        # Actual processing
        coords.append([int(plek) for plek in plekke])
# Print out the user-entered locations
    if verbose:
        size = (max(coords, key=lambda x: x[0])[0],
                max(coords, key=lambda x: x[1])[1])
        for y in range(size[1]+1):
            for x in range(size[0]+1):
                if [x, y] in coords:
                    print(coords.index([x, y]), end="")
                else:
                    print(".", end="")
            print()

# Convert the user-entered locations into a distance matrix
    for i, from_location in enumerate(distances):
        for j, to_location in enumerate(distances):
            if locations[i] != IN_TRANSIT and locations[j] != IN_TRANSIT:
                # Calculate the grid-wise distance. It's easier than the euclidean
                # TODO Convert this distance calculation to use the euclidean formula

                dist = abs(coords[i-1][0] - coords[j-1][0]) + \
                       abs(coords[i-1][1] - coords[j-1][1])  # -1 from the index to account for the smaller matrix size
                distances[i][j] = dist
    return distances



class Driver(object):
    def __init__(self, name, home):
        self.name = name
        self.home = home


driver_A = Driver("Driver A", 1)
driver_B = Driver("Driver B", 2)
driver_schedules = {driver_A.name: [driver_A.home for _ in range(TIME_STEPS)],
                    driver_B.name: [driver_B.home for _ in range(TIME_STEPS)]}

get_distances_matrix(True)
def change_schedule(driver, location, start_incl, end_excl):
    driver_schedules[driver.name][start_incl:end_excl] = \
        [location for _ in range(end_excl - start_incl)]
