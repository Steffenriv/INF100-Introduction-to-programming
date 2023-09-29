import csv

rows = [
      ["Come Together", 4, 20, "Lennon/McCartney"],
      ["Something", 3, 3, "Harrison"],
      ["Maxwell's Silver Hammer", 3, 27, "Lennon/McCartney"],
      ["Oh! Darling", 3, 26, "Lennon/McCartney"],
      ["Octopus's Garden", 2, 51, "Starr"],
      ["I want you", 7, 47, "Lennon/McCartney"],
  ]

def write_to_csv(file, list):
    with open(f"{file}", "w", newline='') as f:
        writer = csv.writer(f) # fra https://www.pythontutorial.net/python-basics/python-write-csv-file/ 15.11.2021
        writer.writerows(list)
        f.close()
    return "done"

print(write_to_csv("Abbey_Road.csv", rows)) 