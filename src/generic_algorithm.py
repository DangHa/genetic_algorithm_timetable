## Author: Ha
## Module: genetic_algorithms

import random, math
import make_timetable

NumberOfInit = 10   # Initialization
NumberOfParent = 3  # Crossover
# Fit score
FitOfTeacher = 1
FitOfStudent = 2

def generic_algorithm (inputML, inputRoom, NumberOfLoop):
    result = []

    # ---  Initialization ---
    # Create N init element timetable
    init = initialization(inputML, inputRoom, NumberOfInit)
    temp_timetables = init[0]
    room = init[1]

    # Begin the evolution
    for i in range(0, NumberOfLoop):

        # --- Fitness ---
        fit = fitness(temp_timetables)
        print(fit)

        # ---- GET RESULT -----
        # get the best result of this round
        result = temp_timetables[fit.index(min(fit))].copy()
        
        if min(fit) == 0 or i == NumberOfLoop-1: #have already had the result
            print("The best fit score: ", min(fit))
            print("The number of loop: ", i+1)
            break 

        # --- Selection ---
        selection(fit, temp_timetables)
        print(fit)

        # --- Crossover ---
        crossover(fit, temp_timetables, NumberOfParent, room)

        # --- Mutation ---
        # if the teacher time is suitable -> dont mutation
        bestTable = temp_timetables[fit.index(min(fit))]
        for i in range(0, len(bestTable)):
            if bestTable[i][6] == False:
                mutation(fit, temp_timetables, inputML, inputRoom, room)
                break

    return result

# delete (len(temp_timetables) - NumberOfInit) elements has the highest fit score
def selection(fit, temp_timetables):
    print("-- Selection --")
    Remover = len(temp_timetables) - NumberOfInit

    for i in range(0, Remover):
        lessFit = 0 
        for j in range(1, len(fit)):
            if fit[j] > fit[lessFit]:
                lessFit = j
        
        del fit[lessFit]
        del temp_timetables[lessFit]


# select 2 best fit 
# create (2) new crossovers by each itself and create 1 new crossover by both
def crossover(fit, temp_timetables, NumberOfParent, room):
    print("-- Crossover --")
    tempFit = fit.copy()

    # create N new crossovers by each itself
    for i in range(0, NumberOfParent):
        if min(tempFit) == math.inf:
            break

        maxElem = tempFit.index(min(tempFit))
        tempFit[maxElem] = math.inf

        improveTimeTable = make_timetable.improve_timetable(temp_timetables[maxElem], fit, room[maxElem])
        temp_timetables.append(improveTimeTable)


# max mutation: create N new random temporary timetables to avoid the local maximum
# P = max(total(identicalFit))/total(fit)
def mutation(fit, temp_timetables, ML, Room, room):
    print("-- Mutation --")
    maxDup = maxDuplicationOfFit(fit)

    pick = random.randint(0, len(fit))
    if pick < maxDup//2:
        print("* Max mutation *")

        # delete all element of temp_timetables and run initialization again  
        # avoid the local maximum
        if maxDup >= len(fit)-1:
            print("* Best Mutation *")
            temp_timetables.clear()
        
        # make N mutation element  
        for i in range(0, maxDup):
            newTempTimetable = []
            while newTempTimetable == []:
                newTempTimetable = make_timetable.make_new_timetable(ML, Room)
                temp_timetables.append(newTempTimetable[0])
                room.append(newTempTimetable[1])

# return array that consist the fit of each temporary timetable
# the point of temporary timetable is the higher, the fit of one is the lower
def fitness(temp_timetables):
    print("-- Fitness --")
    
    result = []

    # evaluate TheFit
    for i in range(len(temp_timetables)):
        temp = temp_timetables[i]
        # set TheFit of all is True
        for j in range(len(temp)):
            temp[j][6] = True
            temp[j][8] = True

        TheFit = the_fit_of_one(temp)
        result.append(TheFit)

    return result

def the_fit_of_one(temp_timetable):
    if len(temp_timetable) == 0:
        return math.inf

    for i in range(len(temp_timetable)-1):
        for j in range(i+1, len(temp_timetable)):
            temp1 = temp_timetable[i]
            temp2 = temp_timetable[j]
            # check whether timetable has same teacher and block
            if temp1[1] == temp2[1] and temp1[4] == temp2[4]:
                # check whether have same period
                if temp1[5] < temp2[5]:
                    if temp1[5]+temp1[2] > temp2[5]:
                        temp1[6] = False
                        temp2[6] = False
                else:
                    if temp2[5]+temp2[2] > temp1[5]:
                        temp1[6] = False
                        temp2[6] = False

            # check whether timetable has same class and block
            if temp1[7] == temp2[7] and temp1[4] == temp2[4] and temp1[9] != temp2[9]:
                # check whether have same period
                if temp1[5] < temp2[5]:
                    if temp1[5]+temp1[2] > temp2[5]:
                        temp1[8] = False
                        temp2[8] = False
                else:
                    if temp2[5]+temp2[2] > temp1[5]:
                        temp1[8] = False
                        temp2[8] = False

    TheFit = 0
    for i in range(0, len(temp_timetable)):
        if temp_timetable[i][6] == False:
            TheFit += FitOfTeacher
        if temp_timetable[i][8] == False:
            TheFit += FitOfStudent

    return TheFit


# Initialization function
def initialization(ML, Room, numberOfInit):
    print("-- Initialization --")

    timetable = []
    room = []
    for i in range(numberOfInit):
        # Create a random room array
        newTempTimetable = make_timetable.make_new_timetable(ML, Room)
        timetable.append(newTempTimetable[0])
        room.append(newTempTimetable[1])

    return [timetable, room]

# get max duplicate item in list
def maxDuplicationOfFit(fit):
    maxDup = 0
    for i in range(len(fit)-1):
        duplication = 1
        for j in range(i+1, len(fit)):
            if fit[i] == fit[j]:
                duplication += 1

        if duplication > maxDup:
            maxDup = duplication
    
    return maxDup