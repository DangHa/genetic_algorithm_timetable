def write_file(data, outputFile):
    # open the file for writing, create if it doesnt exist
    f = open(outputFile, "w+")

    # write data into file
    for i in range(len(data)):
        f.write("\n -------------------- \n")
        for j in range(len(data[i])):
            oneClass = str(data[i][j][0]) + " " + str(data[i][j][1]) + " " + str(data[i][j][2]) + " " + str(data[i][j][3]) + " " + str(data[i][j][4])
            f.write(oneClass + "\n")

    # close file
    f.close()