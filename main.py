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

# TODO refactor everything to only ever use id's, of locations, drivers, etc
# TODO Try to have the program be more dynamic. If a user enters an id greater than all the others, work with it.
IN_TRANSIT = "IN_TRANSIT"
TIME_STEPS = 100
locations = ["IN_TRANSIT",
             "Home A",
             "Home B",
             "School",
             "Rugby",
             "Hockey"]



class Driver(object):
    def __init__(self, name, home):
        self.name = name
        self.home = home


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
        for y in range(size[1] + 1):
            for x in range(size[0] + 1):
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

                dist = abs(coords[i - 1][0] - coords[j - 1][0]) + \
                       abs(coords[i - 1][1] - coords[j - 1][
                           1])  # -1 from the index to account for the smaller matrix size
                distances[i][j] = dist
    return distances


def get_schedules_from_user(verbose=False):
    while True:
        input_string = input("driver_name, location_id, from, until: ")
        if len(input_string) == 0:
            break
        driver_name = input_string.split(" ")[0]
        changes = [int(num) for num in input_string.split(" ")[1:]]

        change_schedule(driver_name, changes[0], changes[1], changes[2])
        if verbose:
            print("{}'s new schedule:\n{}".format(driver_name, driver_schedules[driver_name]))

    # if verbose:
    # TODO add verbose print-out


def change_schedule(driver_name, location, start_incl, end_excl):
    driver_schedules[driver_name][start_incl:end_excl] = \
        [location for _ in range(end_excl - start_incl)]


driver_a = Driver("a", 1)
driver_b = Driver("b", 2)
driver_schedules = {driver_a.name: [driver_a.home for _ in range(TIME_STEPS)],
                    driver_b.name: [driver_b.home for _ in range(TIME_STEPS)]}

# get_distances_matrix(True)
get_schedules_from_user(verbose=True)
