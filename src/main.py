# import other files
from src import read, make_timetable, write


def main(inputMLFile, inputRoomFile):
    # get the data consisting of Malop and Room
    inputML = read.read_ML(inputMLFile)
    inputRoom = read.readRoom(inputRoomFile)

    print(inputML)
    print(inputRoom)

    # create temporary timetable for running generation algorithm
    numberOfTimetable = 10
    temp_timetable = make_timetable.create_temporary_timetable(inputML, inputRoom, numberOfTimetable)

    print(temp_timetable)
    # run GA
    # writing final timetable into file

    write.write_file(temp_timetable)


if __name__ == "__main__":
    main("file/inputML.txt", "file/inputRoom.txt")
