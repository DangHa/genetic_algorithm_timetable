import random, make_timetable

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
        for j in range(len(fit)):
            if fit[j] == 0:
                result.append(temp_timetables[j])
        
        if result != []:
            break

        # --- Selection ---
        Remover = 2
        selection(fit, temp_timetables, Remover)
        print(fit)

        # --- Crossover ---
        crossover(fit, temp_timetables, inputRoom)

        # --- Mutation ---
        mutation()


    return temp_timetables


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
def crossover(fit, temp_timetables, inputRoom):
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
        improveTimeTable = make_timetable.remake_timetable(selectedTimeTable[i], inputRoom)
        temp_timetables.append(improveTimeTable)

    # create 1 new crossover by both


def mutation():
    print("-- Mutation --")

# return array that consist the fit of each temporary timetable
# the point of temporary timetable is the higher, the fit of one is the lower
def fitness(temp_timetables):
    print("-- Fitness --")
    
    result = []

    for i in range(len(temp_timetables)):
        TheFit = the_fit_of_one(temp_timetables[i])
        result.append(TheFit)

    return result

def the_fit_of_one(temp_timetable):
    for i in range(0, len(temp_timetable)-1):
        for j in range(i+1, len(temp_timetable)):
            temp1 = temp_timetable[i]
            temp2 = temp_timetable[j]
            # check whether have same teacher and block
            if temp1[1] == temp2[1] and int(temp1[4]) == int(temp2[4]):
                # check whether have same period
                if int(temp1[5]) < int(temp2[5]):
                    if int(temp1[5])+int(temp1[2]) > int(temp2[5]) and int(temp1[5])+int(temp1[2]) < int(temp2[5]) + int(temp2[2]):
                        temp1[6] = False
                        temp2[6] = False
                else:
                    if int(temp2[5])+int(temp2[2]) > int(temp1[5]) and int(temp2[5])+int(temp2[2]) < int(temp1[5]) + int(temp1[2]):
                        temp1[6] = False
                        temp2[6] = False

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
        random.shuffle(Room)
        newTempTimetable = make_timetable.make_new_timetable(ML, Room)
        result.append(newTempTimetable)

    return result