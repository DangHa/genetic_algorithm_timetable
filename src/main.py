# import other files
import io_excel_file, generic_algorithm
from datetime import datetime

def main(inputMLFile, inputRoomFile, outputFile):

    # get the data consisting of Malop and Room
    inputML = io_excel_file.read_ML(inputMLFile)
    inputRoom = io_excel_file.read_Room(inputRoomFile)

    # run GA
    NumberOfLoop = 200
    
    start = datetime.now()
    result_timetable = generic_algorithm.generic_algorithm(inputML, inputRoom, NumberOfLoop)
    print ("Running time: ", datetime.now()-start)

    # writing final timetable into file
    io_excel_file.write_file(result_timetable, outputFile)

if __name__ == "__main__":
    
    main("file/inputML.csv", "file/inputRoom.txt", "file/output.csv")
    

