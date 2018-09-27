# Input:
#     [[Mã lớp, Giảng viên, Số tiết]]
#     [[Phòng học, Buổi, SoTietConLai]]
# Output:
#     [[Mã lớp, Giảng viên, Phòng, Buổi, Số tiết]]
#     [] if cant make
import random

def create_temporary_timetable(ML, Room, numberOfTimetable):
    result = []

    for i in range(numberOfTimetable):
        random.shuffle(Room)
        newTempTimetable = make_new_timetable(ML, Room)
        result.append(newTempTimetable)

    return result


def make_new_timetable(ML, Room):
    result = []

    for i in range(len(ML)):
        for j in range(len(Room)):
            if Room[j][2] >= int(ML[i][2]):
                MLHaveRoom = ML[i] + Room[j][:2]
                result.append(MLHaveRoom)
                Room[j][2] -= int(ML[i][2])
                break

            # cant make timetable with this ML and Room
            if Room[j][2] <= int(ML[i][2]) and j == len(Room)-1:
                return []

    return result

