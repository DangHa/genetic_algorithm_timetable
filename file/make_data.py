import pandas, random

def make_sample_data(inputDir, outputDir):
    inputML = pandas.read_csv(inputDir).sort_values(by = 'So Tiet', ascending = False)
    
    ML = inputML[inputML.columns[0]].values
    Teacher = inputML[inputML.columns[1]].values
    ST = inputML[inputML.columns[2]].values
    Class = inputML[inputML.columns[3]].values
    
    giaovienthem = ['Nguyen Kim Khanh', 'Ngo Lam Trung', 'Trinh Van Loan', 'Nguyen Phu Binh', 'Nguyen Huu nam Duong', 'Nguyen Thanh Kien', 'Nguyen Hong Quang', 'Do thi Thu Trang', 'La The Vinh', 'Tran Tuan Vinh', 'Bui Quoc Anh', 'Pham Ngoc Hung', ' Tran Trung Kien', 'Nguyen Thi Thanh Nga', 'Le Xuan Thanh', 'Nguyen Duc Tien', 'NGuyen DInh Thuan', 'Nguyen Van Thuan']
    data = all_teacher(Teacher) + giaovienthem
    data1 = make_new(data)
    print(len(data1))
    # random.shuffle(Teacher)
    df = pandas.DataFrame({
        'ML': ML,
        'Giao Vien': data1,
        "So Tiet": ST,
        "Lop": Class
    })

    df.to_csv(outputDir)
    return 

def make_new(giaovienthem):
    result = []
    for i in giaovienthem:
        for j in range(503//len(giaovienthem)+1):
            result.append(i)

    if len(result) != 503:
        for i in range(503- len(result)):
            result.append('Le Ba Vui')

    return result

# all teacher names
def all_teacher(teacher):
    result = []

    for i in range(len(teacher)):
        choose = True
        for j in range(len(result)):
            if result[j] == teacher[i]:
                choose = False
                break

        if choose:
            result.append(teacher[i])

    return result

if __name__ == "__main__":
    make_sample_data("inputML.csv", "inputML.csv")