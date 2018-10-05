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
        selection()

        # --- Crossover ---
        crossover()

        # --- Mutation ---
        mutation()


    return result


def crossover():
    print("-- Crossover --")

def selection():
    print("-- Selection --")

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