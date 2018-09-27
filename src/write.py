def write_file(data):
    # open the file for writing, create if it doesnt exist
    f = open("file/output.txt", "w+")

    # write data into file
    for i in range(len(data)):
        f.write("\n -------------------- \n")
        for j in range(len(data[i])):
            oneClass = str(data[i][j][0]) + " " + str(data[i][j][1]) + " " + str(data[i][j][2]) + " " + str(data[i][j][3]) + " " + str(data[i][j][4])
            f.write(oneClass + "\n")

    # close file
    f.close()


def main() :
    write_file("This is line\r\n")

# if this file is being imported frome another module,
# __name__ will be set to the module's name
# VD: when main.py run -> __name__ in here will be "write"
if __name__ == "__main__":
    main()
