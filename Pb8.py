# -*- coding: utf-8 -*-
"""
Created on Thu May 24 14:37:05 2018

@author: user
"""

import random
import pylab

# Global Variables
#MAXRABBITPOP = 1000
#CURRENTRABBITPOP = 500
#CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    #There are never fewer than 10 rabbits; the maximum population of rabbits is 1000
    #each rabbit during each time step, a new rabbit will be born with a probability of
    #probability = 1-(CURRENTRABBITPOP/MAXRABBITPOP)
    newBornRabbits = 0
    for n in range(CURRENTRABBITPOP):
        if random.random() <= 1-(CURRENTRABBITPOP/MAXRABBITPOP):
            newBornRabbits += 1
    if CURRENTRABBITPOP + newBornRabbits > MAXRABBITPOP:
        CURRENTRABBITPOP = MAXRABBITPOP
    else:
        CURRENTRABBITPOP += newBornRabbits
    

        
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    #There are never fewer than 10 foxes.
    #At each time step, after the rabbits have finished reproducing,
    #a fox will try to hunt a rabbit with success rate of
    # probability = CURRENTRABBITPOP/MAXRABBITPOP
    #If a fox succeeds in hunting, it will decrease the number of rabbits
    #by 1 immediately. Remember that the population of rabbits is never lower than 10.
    #Additionally, if a fox succeeds in hunting, then it has a 1/3 probability
    #of giving birth in the current time-step.
    #If a fox fails in hunting then it has a 10 percent chance of dying
    #in the current time-step.
    #If the starting population is below 10 then you should do nothing.
    #You should not increase the population nor set the population to 10.

    if CURRENTFOXPOP <= 10:
        pass
    else:
        newBornFoxes, deadFoxes = 0, 0
        for n in range(CURRENTFOXPOP):
            if random.random() <= CURRENTRABBITPOP/MAXRABBITPOP and CURRENTRABBITPOP > 10:
                CURRENTRABBITPOP -= 1
                if random.random() <= 1/3:
                    newBornFoxes += 1
            if random.random() <= 1/10:
                deadFoxes += 1
        deltaFoxes = newBornFoxes - deadFoxes
        if CURRENTFOXPOP - deltaFoxes < 10:
            CURRENTFOXPOP = 10
        else:
            CURRENTFOXPOP += deltaFoxes
    
    
    
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    
    rabbit_populations, fox_populations = [], []
    for n in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    return rabbit_populations, fox_populations

MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30
numSteps = 200

rabbitPopulationOverTime, foxPopulationOverTime = runSimulation(numSteps)
pylab.plot(rabbitPopulationOverTime, 'b-', label='Rabbit Population')
pylab.plot(foxPopulationOverTime, 'r-', label='Fox Population')
pylab.legend(loc = "best")


coeff = pylab.polyfit(range(len(rabbitPopulationOverTime)), rabbitPopulationOverTime, 2)
pylab.plot(pylab.polyval(coeff, range(len(rabbitPopulationOverTime))))
coeff = pylab.polyfit(range(len(foxPopulationOverTime)), foxPopulationOverTime, 2)
pylab.plot(pylab.polyval(coeff, range(len(foxPopulationOverTime))))
