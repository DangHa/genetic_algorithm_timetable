# Input:
#     [[Mã lớp, Giảng viên, Số tiết]]
#     [[Phòng học, Buổi, Số tiết còn lại]]
# Output:
#     [[Mã lớp, Giảng viên, Số tiết, Phòng, Buổi, Tiết bắt đầu, TheFit]]
#     [] - if cant create

# De tang hieu qua toi da day xep tat ca ML co nhieu tiet vao truoc
# Output khong co trung phong hop va thoi gian ma chi con trung thoi gian cua giao vien

def make_new_timetable(ML, Room):
    result = []

    for i in range(len(ML)):
        for j in range(len(Room)):
            if Room[j][2] >= int(ML[i][2]):
                MLHaveRoom = ML[i] + Room[j][:2] + [7-Room[j][2], True]
                result.append(MLHaveRoom)
                Room[j][2] -= int(ML[i][2])
                break

            # cant make timetable with this ML and Room
            if Room[j][2] <= int(ML[i][2]) and j == len(Room)-1:
                revert_Room(Room)
                return []

    revert_Room(Room)
    return result

# revert the So_Tiet_Con_lai of Room
def revert_Room(Room):
    for i in range(len(Room)):
        Room[i][2] = 6