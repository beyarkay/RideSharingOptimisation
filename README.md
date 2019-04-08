# RideSharingOptimisation
Various attempt at solving a ride sharing optimisation problem.

##Outline
Parents of school children want to form a ride sharing group. However it is very difficult to organise a schedule with anything more than a trivial number of parents / children

###Objective
* Achieve fewer hours worth of driving per parent, preferably on as few days as possible

##Variables to Consider
1. Children's schedule
2. Parent's schedule
3. Parent preference 
    * do you prefer 1 hour in traffic or 2 hours on open roads?
4. Car size 
5. Pickup and drop-off locations
6. Time to drive between locations
    * Traffic
7. The driving-hour standard deviation should be able to be specified:
    * Everyone's total driving time should be within, say, 1 hour of everyone else's
8. Each parent will be happier driving their own child, maybe even if they end up driving a lot longer than everyone else
    
### Possibilities for Optimisation
* Every parent and child will always start & end at the same place 

    
##Simplification of the Problem
Initially, the project will focus only on a simplified version of the problem:
* Many of the variables (3, 7, 8) are up to parent preference, which cannot be quantified effectively. Therefore, multiple 
