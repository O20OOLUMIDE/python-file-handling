"""
File handling example in Python.
Writes data to a text file, then reads it back.
"""

def write_data():
    filename = "program_data.txt"
    with open(filename, "w") as text_file:
        text_file.write("Craig\n")
        text_file.write("n\n")
        text_file.write("Dave\n")


def read_data():
    filename = "program_data.txt"
    with open(filename, "r") as text_file:
        for line in text_file:
            print(line.strip())


if __name__ == "__main__":
    write_data()
    read_data()
