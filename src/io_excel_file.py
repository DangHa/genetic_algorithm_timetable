import pandas

# output: ["PhongHoc", "BuoiThuMay", "SoTietConLai"]
def read_Room(fileDir):
    # open the file and set it can be read
    f = open(fileDir, "r")

    result = []

    if f.mode == 'r':
        # read file line by line
        contents = f.readlines()
        for line in contents:
            for i in range(11):
                room = [line[:len(line)-1], i+1, 6]
                result.append(room)

    # close file
    f.close()

    return result

# output: ["Malop", "GiangVien", "Lop sinh vien", "Sotiet"]
def read_ML(fileDir):
    inputML = pandas.read_csv(fileDir).sort_values(by = 'So Tiet', ascending = False)
    return inputML.values.tolist()

# print: ["Malop", "GiangVien", "Lop sinh vien", "Sotiet",
#           "Phong Hoc", "Buoi Thu May", "Tiet bat dau",
#           "Fit Giang Vien"]
def write_file(data, outputFile):
    columns = ['ML', 'Giang Vien', 'So Tiet', 'Phong', 'Buoi', 'Tiet Bat Dau', 'Fit of Giang Vien', 'Lop Sinh Vien', 'Fit of Sinh Vien']
    df = pandas.DataFrame(data, columns=columns)
    df.to_csv(outputFile)

if __name__ == "__main__":
    result = read_ML("file/inputML.csv")
    print(result)

