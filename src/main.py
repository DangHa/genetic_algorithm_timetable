# import other files
from src import read, make_timetable


def main():
    # get the data consisting of Malop and Room
    inputML = read.read_ML("file/inputML.txt")
    inputRoom = read.readRoom("file/inputRoom.txt")

    print(inputML)
    print(inputRoom)

    # make temporary timetable for running generation algorithm
    temp_timetable = make_timetable.make_new_timetable(inputML, inputRoom)

    print(temp_timetable)
    # run GA
    # writing final timetable into file


if __name__ == "__main__":
    main()
