import random, make_timetable

def generic_algorithm (inputML, inputRoom):

    # ---  Initialization  ---
    # This routine creates a population of N timetable
    N = 10
    temp_timetable = initialization(inputML, inputRoom, N)
    print(temp_timetable)



    return temp_timetable


# def crossover()

# def selecting_table()

# def mutation()

# def fitness()

# def initialization()



def initialization(ML, Room, numberOfInit):
    result = []

    for i in range(numberOfInit):
        # Create a random room array
        random.shuffle(Room)
        newTempTimetable = make_timetable.make_new_timetable(ML, Room)
        result.append(newTempTimetable)

    return result