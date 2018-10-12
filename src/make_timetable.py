# Input:
#     [[Mã lớp, Giảng viên, Số tiết]]
#     [[Phòng học, Buổi, Số tiết còn lại]]
# Output:
#     [[Mã lớp, Giảng viên, Số tiết, Phòng, Buổi, Tiết bắt đầu, TheFit]]
#     [] - if cant create

# De tang hieu qua toi da day xep tat ca ML co nhieu tiet vao truoc
# Output khong co trung phong hop va thoi gian ma chi con trung thoi gian cua giao vien
import random

def make_new_timetable(ML, Room):
    result = []

    tempRoom = [x[:] for x in Room]
    random.shuffle(tempRoom)

    for i in range(len(ML)):
        for j in range(len(tempRoom)):

            if tempRoom[j][2] >= ML[i][2]:
                MLHaveRoom = ML[i] + tempRoom[j][:2] + [7-tempRoom[j][2], True]
                result.append(MLHaveRoom)
                tempRoom[j][2] -= ML[i][2]
                break

            # cant make timetable with this ML and Room
            if tempRoom[j][2] < ML[i][2] and j == len(tempRoom)-1:
                return []

    return result

def remake_timetable(selectedTimeTable):
    result = [x[:] for x in selectedTimeTable]

    # everyone's schedule
    schedule = scheduleEveryOne(selectedTimeTable)

    # get a class have the false TheFit
    falseML = []
    positionOfFasleML = 0
    for i in range(len(selectedTimeTable)):
        if selectedTimeTable[i][6] == False:
            falseML = selectedTimeTable[i][:]
            positionOfFasleML = i
            
    # change with other one with schdule can add the falseML
    for i in range(len(schedule)):
        if falseML[1] != schedule[i][0]:
            choose = checkSchedule(falseML, schedule[i])

            if choose == True:
                # finding schedule of one have faleML
                scheduleOfFalseML = []
                for k in range(len(schedule)):
                    if schedule[k][0] == falseML[1]:
                        scheduleOfFalseML = schedule[k]
                        break

                # finding a ML of this selected person can change with falseML
                for j in range(len(result)):
                    # ML doi cua nguoi duoc chon khong trung voi nguoi muon doi
                    # ML doi cung SoTiet voi ML chon
                    if result[j][1] == schedule[i][0] and checkSchedule(result[j], scheduleOfFalseML) == True and result[j][2] == falseML[2]:
                        # change time and room
                        temp = result[j]
                        result[j] = temp[:3] + result[positionOfFasleML][3:]
                        result[positionOfFasleML] = result[positionOfFasleML][:3] + temp[3:]
                        break

    return result

def checkSchedule(ML, schedule):
    choose = True

    for j in range(1, len(schedule)):
        # check whether have same block
        if schedule[j][1] == ML[4]:
            # check whether have same period
            if schedule[j][2] < ML[5]:
                if schedule[j][2]+schedule[j][3] > ML[5]:
                    choose = False
                    break
            else:
                if  ML[5] + ML[2] > schedule[j][2]:
                    choose = False
                    break
    
    return choose

# schedule of one: [name, [ML, Buoi, TietBatDau, SoTiet], [], [], ...]
# output: [schedule of every one]
def scheduleEveryOne(selectedTimeTable):
    result = []

    temp = [x[:] for x in selectedTimeTable]

    while len(temp) != 0:
        scheduleOfOne = [temp[0][1]]

        remove = []
        for i in range(len(temp)):
            if temp[i][1] == scheduleOfOne[0]:

                Class = [temp[i][0], temp[i][4], temp[i][5], temp[i][2]]
                scheduleOfOne.append(Class)
                remove.append(temp[i][0])

        for i in range(len(remove)):
            for j in range(len(temp)):
                if temp[j][0] == remove[i]:
                    del temp[j]
                    break
        
        result.append(scheduleOfOne)
    
    return result
