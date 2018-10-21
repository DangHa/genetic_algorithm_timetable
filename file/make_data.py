import pandas, random

def make_sample_data(inputDir, outputDir):
    inputML = pandas.read_csv(inputDir).sort_values(by = 'So Tiet', ascending = False)
    
    ML = inputML[inputML.columns[0]].values
    Teacher = inputML[inputML.columns[1]].values
    ST = inputML[inputML.columns[2]].values
    Class = inputML[inputML.columns[3]].values
    hp = inputML[inputML.columns[4]].values

    # random.shuffle(Teacher)
    df = pandas.DataFrame({
        'ML': ML,
        'Giao Vien': Teacher,
        "So Tiet": ST,
        "Lop": Class,
        "HP": hp
    })

    df.to_csv(outputDir)
    return 


if __name__ == "__main__":
    make_sample_data("inputML.csv", "inputML.csv")