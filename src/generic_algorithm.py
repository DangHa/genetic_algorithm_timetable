import random, math
import make_timetable

def generic_algorithm (inputML, inputRoom, NumberOfLoop):
    result = []

    # ---  Initialization ---
    # Createing a the N init element timetable
    N = 10
    temp_timetables = initialization(inputML, inputRoom, N)

    # Begining the evolution
    for i in range(0, NumberOfLoop):

        # --- Fitness ---
        fit = fitness(temp_timetables)
        print(fit)

        # check whether we have a result
        for j in range(len(fit)):
            if fit[j] <= 1:
                result.append(temp_timetables[j])
                
        if result != []: #have had the result
            break

        # --- Selection ---
        Remover = 2
        if len(temp_timetables) != N:
            Remover = len(temp_timetables) - N #have mutated

        selection(fit, temp_timetables, Remover)
        print(fit)

        # --- Crossover ---
        crossover(fit, temp_timetables)

        # --- Mutation ---
        # pick one temporary timetable
        picked_timatable = temp_timetables[random.randint(0,7)]
        mutation(picked_timatable)

        # avoid the local maximum
        NumberOfMutation = 2
        max_mutation(fit, temp_timetables, inputML, inputRoom, NumberOfMutation)

        # totaly avoid the local maximum
        best_mutation(fit, temp_timetables, inputML, inputRoom, N)

    return result


def selection(fit, temp_timetables, Remover):
    print("-- Selection --")

    for i in range(0, Remover):
        lessFit = 0 
        for j in range(1, len(fit)):
            if fit[j] > fit[lessFit]:
                lessFit = j
        
        del fit[lessFit]
        del temp_timetables[lessFit]

# select 2 best fit 
# create (2) new crossovers by each itself and create 1 new crossover by both
def crossover(fit, temp_timetables):
    print("-- Crossover --")

    # 2 best fit
    selectedTimeTable = [] 

    bestFit1 = 1
    for j in range(2, len(fit)):
        if fit[j] < fit[bestFit1]:
            bestFit1 = j
    selectedTimeTable.append(temp_timetables[bestFit1])

    bestFit2 = 0
    for j in range(1, len(fit)):
        if fit[j] < fit[bestFit2] and j != bestFit1:
            bestFit2 = j
    selectedTimeTable.append(temp_timetables[bestFit2])

    # create (2) new crossovers by each itself
    for i in range(0, len(selectedTimeTable)):
        improveTimeTable = make_timetable.remake_timetable(selectedTimeTable[i])
        temp_timetables.append(improveTimeTable)
 
    # create 1 new crossover by both


def mutation(picked_timatable):
    print("-- Mutation --")

    if len(picked_timatable) == 0:
        return

    # pick 2 random elements
    temp1 = picked_timatable[random.randint(0, len(picked_timatable)-1)]
    temp2 = picked_timatable[random.randint(0, len(picked_timatable)-1)]

    if temp1[2] == temp2[2] :
        print("* New Mutation *")
        temp = temp1
        temp1 = temp1[:3] + temp2[3:]
        temp2 = temp2[:3] + temp[3:]

# max mutation: create N new random temporary timetables
# to avoid the local maximum
# P = max(total(identicalFit))/total(fit)
def max_mutation(fit, temp_timetables, ML, Room, N):
    maxDup = maxDuplicationOfFit(fit)

    pick = random.randint(0, len(fit)-1)
    if pick < maxDup:
        print("* Max mutation *")
        # make N mutation
        for i in range(0, N):
            newTempTimetable = []
            while newTempTimetable == []:
                newTempTimetable = make_timetable.make_new_timetable(ML, Room)
                temp_timetables.append(newTempTimetable)

# best mutation: delete all element of temp_timetables and run initialization again 
# to avoid local maximum that max mutation can't exit
def best_mutation(fit, temp_timetables, ML, Room, N):
    maxDup = maxDuplicationOfFit(fit)

    if maxDup >= len(fit)/2:
        print("* Best mutaion *")
        # delete all
        for i in range(len(temp_timetables)):
            del temp_timetables[0]

        temp_timetables += initialization(ML, Room, N)

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
            # check whether have same teacher and block
            if temp1[1] == temp2[1] and temp1[4] == temp2[4]:
                # check whether have same period
                if temp1[5] < temp2[5]:
                    if temp1[5]+temp1[2] > temp2[5] and temp1[5]+temp1[2] < temp2[5] + temp2[2]:
                        temp_timetable[i][6] = False
                        temp_timetable[j][6] = False
                else:
                    if temp2[5]+temp2[2] > temp1[5] and temp2[5]+temp2[2] < temp1[5] + temp1[2]:
                        temp_timetable[i][6] = False
                        temp_timetable[j][6] = False

    TheFit = 0
    for i in range(0, len(temp_timetable)):
        if temp_timetable[i][6] == False:
            TheFit += 1

    return TheFit


# Initialization function
def initialization(ML, Room, numberOfInit):
    print("-- Initialization --")
    
    result = []

    for i in range(numberOfInit):
        # Create a random room array
        newTempTimetable = make_timetable.make_new_timetable(ML, Room)
        result.append(newTempTimetable)

    return result

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