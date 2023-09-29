
def rename_from_data(filename):
    fileinfo = []
    with open(f"{filename}", encoding="utf8") as file:
        for line in file:
            fileinfo.append(line)
    file.close()
    sted = fileinfo[0]
    dato = fileinfo[1]
    nytt_filnavn = f"{str(dato).strip()}_{str(sted).strip()}.txt"
    nyfil = open(f"{nytt_filnavn}", "w")
    fileinfo.remove(fileinfo[0])
    fileinfo.remove(fileinfo[0])        #må fjerne 0 igjen for å fjerne det som opprinnelig var linje 2, men som no har blitt 1 etter forgje kodelinje.
    nyfil.write(''.join(fileinfo))
    nyfil.close()
    return nytt_filnavn

def rename_all(namelist):
    length = len(namelist)
    count = 0
    rename = ""
    while count < length:
        rename += rename_from_data(namelist[count])
        count += 1
    return rename

rename_from_data("qwerty.txt")