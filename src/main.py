# import other files
import read, write, generic_algorithm


def main(inputMLFile, inputRoomFile, outputFile):
    
    # get the data consisting of Malop and Room
    inputML = read.read_ML(inputMLFile)
    inputRoom = read.readRoom(inputRoomFile)
    # print(inputML)
    # print(inputRoom)

    # run GA
    NumberOfLoop = 100
    result_timetable = generic_algorithm.generic_algorithm(inputML, inputRoom, NumberOfLoop)

    # writing final timetable into file
    write.write_file(result_timetable, outputFile)

if __name__ == "__main__":
    main("file/inputML.txt", "file/inputRoom.txt", "file/output.txt")
