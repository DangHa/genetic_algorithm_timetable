def write_file(data):
    # open the file for writing, create if it doesnt exist
    f = open("file/output.txt", "w+")

    # write data into file
    for i in range(10):
        f.write(data)

    # close file
    f.close()


def main() :
    write_file("This is line\r\n")

# if this file is being imported frome another module,
# __name__ will be set to the module's name
# VD: when main.py run -> __name__ in here will be "write"
if __name__ == "__main__":
    main()
