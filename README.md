# Ride Sharing Optimisation
Various attempts at solving a ride sharing optimisation problem.

## Outline
Parents of school children want to form a ride sharing group. However it is very difficult to organise an efficient and fair schedule with anything more than a trivial number of parents / children

### Objective
* Achieve fewer hours worth of driving per parent, preferably on as few days as possible

## Variables to Consider
1. Children's schedule
2. Parent's schedule
3. Car size 
4. Pickup and drop-off locations
5. Time to drive between locations
    * Traffic
6. Parent preference 
    * do you prefer 1 hour in traffic or 2 hours on open roads?
7. The driving-hour standard deviation should be able to be specified:
    * Everyone's total driving time should be within, say, 1 hour of everyone else's
8. Each parent will be happier driving their own child, maybe even if they end up driving a lot longer than everyone else
    
### Possibilities for Optimisation
* Every parent and child will always start & end at the same place 

    
## Simplification of the Problem
Initially, the project will focus only on a simplified version of the problem:
* Many of the variables (6, 7, 8) are up to parent preference, which cannot be quantified effectively. To solve this:
    * Return multiple, similar, options to the user, for them to choose from and discuss. 
    * These options should be aesthetically good looking, as the users will likely not be used to command-line outputs. The outward appearance will affect adoption of the program
    * However, for now just focus on the processing. Output can come later
* Assume a schedule that repeats perfectly every 7 days (Monday to Sunday)
* Assume every car seats 4 passengers
* Assume every car can always carry all the baggage of the children (sports equipment, schoolbags, etc)
* Assume the travel-time between locations is constant (ie no traffic)
* Assume only 2 parents and 2 children, to allow manual checking of the solution
* Cars and their drivers can be considered to be one entity
* Only look to solve for the afternoon rides, where children go from school, to a sport, to home
* Use abstract time steps, not hours minutes seconds

## Further Research
Once the above problem has been solved for its search space, the search space will be expanded by eliminating each of the above simplifications, one by one.
### Possible Expansions
* More intuitive / user friendly interface / output
* A schedule that repeats every N days
    * This will be followed quickly by: a schedule that does not repeat
* Variable car sizes
* Variable car baggage capacities
* Variable number of parents
* Variable number of children
* Schedules that covers the entire day
* Use proper time, not just hours minutes seconds