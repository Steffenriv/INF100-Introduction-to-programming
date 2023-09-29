

def open_file(filename):
    output = ""
    with open(f"{filename}", encoding="utf8") as file:
        for line in file:
            output += ">>>"
            output += line.strip()
            output += "<<<\n"
    file.close()
    return output

