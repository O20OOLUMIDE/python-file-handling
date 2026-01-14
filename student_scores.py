# Subroutine to write student data to a file
def WriteData():
    FileName = "class data.txt"
    TextFile = open(FileName, "w")


    for count in range(5):
        name= input("Enter student name: ")
        score = input\("Enter test score: ")
        Textfile.write(name + "," + score + "\n"


    TextFile.close()


# Subroutine to read student data from a file
def ReadData():
    FileName = "class data.txt"
    TextFile = open(Filename, "r")


    for line in TextFile:
        print(line.strip())

    TextFile.close()


# Main program
WriteData()
ReadData()


                       
