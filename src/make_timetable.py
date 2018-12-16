## Author: Ha
## Module: make_and_improve_timetable

# De tang hieu qua toi da day xep tat ca ML co nhieu tiet vao truoc
# Output khong co trung phong hop va thoi gian ma chi con trung thoi gian cua giao vien
import random

## Input:
##     [[Mã lớp, Giảng viên, Số tiết, Lop Sinh Vien]]
##     [[Phòng học, Buổi, Số tiết còn lại]]
## Output:
##     [[Mã lớp, Giảng viên, Số tiết, Phòng, Buổi, Tiết bắt đầu, TheFitOfTeacher,
##                                                   StudentClass,TheFitOfStudent]]
##     [] - if cant create
def make_new_timetable(ML, Room):
    result = []
    tempRoom = [x[:] for x in Room]
    random.shuffle(tempRoom)
    for i in range(len(ML)):
        for j in range(len(tempRoom)):
            if tempRoom[j][2] >= ML[i][2] and tempRoom[j][3] == ML[i][5]:
                MLHaveRoom = ML[i][:3] + tempRoom[j][:2] + [7-tempRoom[j][2], True, ML[i][3], True, ML[i][4], ML[i][5]]
                result.append(MLHaveRoom)
                tempRoom[j][2] -= ML[i][2]
                break

            # cant make timetable with this ML and Room
            if tempRoom[j][2] < ML[i][2] and j == len(tempRoom)-1:
                return [[], tempRoom]

    return [result, tempRoom]

def improve_timetable(selectedTimeTable, fit, room):
    result = [x[:] for x in selectedTimeTable]

    # everyone's schedule
    teacherNames = all_teacher(result)
    random.shuffle(teacherNames)

    # get a class have the false TheFit
    falseML = -1
    for i in range(len(result)):
        if result[i][6] == False:
            falseML = i
            break
    
    # This timetable is suitable for all teacher
    # -> we'll make it fit for student (basis function - advaned function that same with teacher)
    if falseML < 0:
        random.shuffle(result)
        for i in range(len(result)):
            if result[i][8] == False:
                falseML = i
                break

    # -- find a room is free in this time to avoid the local maximum when the main mutation was turn off
    if result[falseML][6] == True and len(set(fit)) == 1:
        random.shuffle(room)
        teacher = teacherSchedule(result, result[falseML][1])
        student = studentSchedule(result, result[falseML][7])
        for i in range(len(room)):
            if room[i][2] >= result[falseML][2] and room[i][1] != result[falseML][4] and room[i][3] == result[falseML][10]:
                newClass = result[falseML][:3] + room[i][:2] + [7-room[i][2]] + result[falseML][6:]
                if check(newClass, teacher) and check(newClass, student):
                    result[falseML] = newClass
                    return result

    # finding schedule of one have faleML
    scheduleOfFalseML = teacherSchedule(result, result[falseML][1])

    for i in range(len(teacherNames)):
        if result[falseML][1] != teacherNames[i]:
            schedule = teacherSchedule(result, teacherNames[i])
            choose = check(result[falseML], schedule)

            if choose == True:
                for j in range(len(result)):
                    # findding ML can change with falseML and fit with time of teacher
                    if result[j][1] == schedule[0] and check(result[j], scheduleOfFalseML) == True and result[j][2] == result[falseML][2] and result[j][10] == result[falseML][10]:
                        # check whether the change is suitable with time of student
                        schedule1 = studentSchedule(result, result[falseML][7])
                        schedule2 = studentSchedule(result, result[j][7])
                        if check(result[j], schedule1) and check(result[falseML], schedule2) and result[j][7] != result[falseML][7]:
                            temp = result[j]
                            result[j] = temp[:3] + result[falseML][3:6] + temp[6:]
                            result[falseML] = result[falseML][:3] + temp[3:6]+ result[falseML][6:]
                            return result
                
    return result

# all teacher names
def all_teacher(selectedTimeTable):
    result = []

    for i in range(len(selectedTimeTable)):
        choose = True
        for j in range(len(result)):
            if result[j] == selectedTimeTable[i][1]:
                choose = False
                break

        if choose:
            result.append(selectedTimeTable[i][1])

    return result

# output: [teacherName, [ML, Buoi, TietBatDau, SoTiet], [], [], ...]
def teacherSchedule(selectedTimeTable, teacherName):
    temp = selectedTimeTable

    result = [teacherName]
    for i in range(len(temp)):
        if temp[i][1] == teacherName:
            Class = [temp[i][0], temp[i][4], temp[i][5], temp[i][2]]
            result.append(Class)
    
    return result

# output: [classname, [ML, Buoi, TietBatDau, SoTiet, HP], [], [], ...]
def studentSchedule(selectedTimeTable, className):
    temp = selectedTimeTable

    result = [className]
    for i in range(len(temp)):
        if temp[i][7] == className:
            Class = [temp[i][0], temp[i][4], temp[i][5], temp[i][2], temp[i][9]]
            result.append(Class)
    
    return result

def check(ML, schedule):
    choose = True

    for j in range(1, len(schedule)):

        # if have the same HP -> Satisfies schedule of both
        if len(schedule[j]) == 5:
            if schedule[j][4] == ML[9] and (schedule[j][1] != ML[4] and schedule[j][2] != ML[5]):
                break

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