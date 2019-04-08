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
TIME_STEPS = 1000
locations = ["-IN TRANSIT-"
             "Home A",
             "Home B",
             "School",
             "Rugby",
             "Hockey"]


# id_to_location = {i: location for i, location in enumerate(locations)}


class Driver(object):
    def __init__(self, name, home):
        self.name = name
        self.home = home


driver_A = Driver("Driver A", 1)
driver_B = Driver("Driver B", 2)
driver_schedules = {driver_A.name: [driver_A.home for _ in range(TIME_STEPS)],
                    driver_B.name: [driver_B.home for _ in range(TIME_STEPS)]}


def change_schedule(driver, location, start_incl, end_excl):
    driver_schedules[driver.name][start_incl:end_excl] = \
        [location for _ in range(end_excl - start_incl)]
