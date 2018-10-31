## Author: Ha
## Module: io_excel_file

import pandas

# output: ["PhongHoc", "BuoiThuMay", "SoTietConLai", "LoaiPhong"]
def readRoom(fileDir):
    inputRoom = pandas.read_csv(fileDir)

    Room = inputRoom[inputRoom.columns[0]].values.tolist()
    RoomType = inputRoom[inputRoom.columns[1]].values.tolist()

    result = []
    for i in range(len(Room)):
        for j in range(11):
            room = [Room[i], j+1, 6, RoomType[i]]
            result.append(room)

    return result

# output: ["Malop", "GiangVien", "Lop sinh vien", "Sotiet"]
def read_ML(fileDir):
    inputML = pandas.read_csv(fileDir).sort_values(by = 'So Tiet', ascending = False)
    return inputML.values.tolist()

# print: ["Malop", "GiangVien", "Lop sinh vien", "Sotiet",
#           "Phong Hoc", "Buoi Thu May", "Tiet bat dau",
#           "Fit Giang Vien"]
def write_file(data, outputFile):
    columns = ['ML', 'Giang Vien', 'So Tiet', 'Phong', 'Buoi', 'Tiet Bat Dau', 'Fit of Giang Vien', 'Lop Sinh Vien', 'Fit of Sinh Vien', 'HP', 'Loai Phong']
    df = pandas.DataFrame(data, columns=columns)
    df.to_csv(outputFile)

if __name__ == "__main__":
    result = readRoom("file/inputRoom.csv")
    print(result)

