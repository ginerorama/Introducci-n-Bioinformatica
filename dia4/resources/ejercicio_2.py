data = open("data.csv")
for line in data:
    columns = line.rstrip("\n").split(",")
    species = columns[0]
    sequence = columns[1]
    name = columns[2]
    expression = columns[3]
    length = len(sequence)
    if length > 90 and length < 110:
        print(name,str(length))

