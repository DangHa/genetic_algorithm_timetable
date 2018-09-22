def read_ML(fileDir):
    # open the file and set it can be read
    f = open(fileDir, "r")

    result = []

    if f.mode == 'r':
        # read file line by line
        contents = f.readlines()
        for line in contents:
            input = data_analyst(line)
            result.append(input)

    # close file
    f.close()

    return result

# input: "Malop GiangVien Sotiet" - String
# output: ("Malop", "GiangVien", "Sotiet") - Tuple
def data_analyst(line):
    result = ()

    point = 0
    for i in range(len(line)):
        if line[i] == " " and line[i+1].isnumeric() == False and point == 0:
            result += (line[point:i], ) # MaLop
            point = i+1
        elif line[i] == " " and line[i+1].isnumeric() == True:
            result += (line[point:i], ) # GiangVien
            point = i+1
            break

    result += (line[point:point+1],) # SoTiet

    return result

def readRoom(fileDir):
    # open the file and set it can be read
    f = open(fileDir, "r")

    result = []

    if f.mode == 'r':
        # read file line by line
        contents = f.readlines()
        for line in contents:
            for i in range(11):
                room = (line[:len(line) - 2], i+1, 0)
                result.append(room)

    # close file
    f.close()

    return result


# test for the read_file module
def main(fileDir) :
    return read_ML(fileDir)

if __name__ == "__main__":
    result = main("file/inputML.txt")
    print(result)