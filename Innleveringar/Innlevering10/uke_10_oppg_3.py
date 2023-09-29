
def r_w_file(infile, outfile):
    with open(f"{infile}", encoding="utf8") as file1:
        output = ""
        tempday = []
        for line in file1:
            day, temp = line.split()
            tempday.append((temp, day))
    file1.close()
    file2 = open(f"{outfile}", "a")
    for i in range(len(tempday)):
        if float(tempday[i][0]) >= 23.5:
            file2.write(tempday[i][1] + " " + tempday[i][0] + "\n")
    file2.close()
    return outfile
