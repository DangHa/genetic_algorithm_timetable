import random, make_timetable

def generic_algorithm (inputML, inputRoom):

    # ---  Initialization  ---
    # This routine creates a population of N timetable
    N = 10
    temp_timetables = initialization(inputML, inputRoom, N)
    # print(temp_timetables)

    fit = fitness(temp_timetables[1])
    print(fit)



    return temp_timetables


def crossover():
    print("crossover")

def selecting_table():
    print("selection")

def mutation():
    print("mutation")

# return array that consist the fit of each temporary timetable
# the point of temporary timetable is the higher, the fit of one is the lower
def fitness(temp_timetable):
    print("fitness")
    
    result = []

    for i in range(0, len(temp_timetable)-1):
        for j in range(i+1, len(temp_timetable)):
            temp1 = temp_timetable[i]
            temp2 = temp_timetable[j]
            # check whether have same teacher and block
            if temp1[1] == temp2[1] and int(temp1[4]) == int(temp2[4]):
                # check whether have same period
                if int(temp1[5]) < int(temp2[5]):
                    if int(temp1[5])+int(temp1[2]) > int(temp2[5]) and int(temp1[5])+int(temp1[2]) < int(temp2[5]) + int(temp2[2]):
                        print(i)
                        print(j)
                        print(temp1)
                        print(temp2)
                        print(" ----- ")
                else:
                    if int(temp2[5])+int(temp2[2]) > int(temp1[5]) and int(temp2[5])+int(temp2[2]) < int(temp1[5]) + int(temp1[2]):
                        print(i)
                        print(j)
                        print(temp1)
                        print(temp2)
                        print(" ----- ")

    return result

# Initialization function
def initialization(ML, Room, numberOfInit):
    print("initialization")

    result = []

    for i in range(numberOfInit):
        # Create a random room array
        random.shuffle(Room)
        newTempTimetable = make_timetable.make_new_timetable(ML, Room)
        result.append(newTempTimetable)

    return result