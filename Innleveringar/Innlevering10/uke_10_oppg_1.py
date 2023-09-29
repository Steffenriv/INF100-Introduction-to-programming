
def open_file(filename):
    file = open(f"{filename}", "r")
    output = ""
    for line in file:
        output += line
    file.close()
    return output

