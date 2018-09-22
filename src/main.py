# import other files
from src import read


def main():
    # get the data consisting of Malop and Room
    inputML = read.read_ML("file/inputML.txt")
    inputRoom = read.readRoom("file/inputRoom.txt")

    # make temporary timetable for running generation algorithm
    # run GA
    # writing final timetable into file
    print(inputML)
    print(inputRoom)

if __name__ == "__main__":
    main()
