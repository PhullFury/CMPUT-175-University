with open('rainfall.txt', 'r') as file:
    line = file.readline().rstrip('\n')
    RainfallInfo = {}
    while not line == "":
        temp = line.split(" ")
        TextVal = f"{temp[0].upper():^25} {float(temp[1]):>5.1f}"
        RainfallInfo[round(float(temp[1]),1)] = TextVal
        line = file.readline().rstrip('\n')

RainfallInfoSorted = dict(sorted(RainfallInfo.items()))

FiftySixty =[]
SixtySeventy = []
SeventyEighty = []
EightyNinety = []
NinetyHun = []

for key in RainfallInfoSorted:
    if (key >= 50 and key < 60):
        FiftySixty.append(RainfallInfoSorted[key])
    if (key >= 60 and key < 70):
        SixtySeventy.append(RainfallInfoSorted[key])
    if (key >= 70 and key < 80):
        SeventyEighty.append(RainfallInfoSorted[key])
    if (key >= 80 and key < 90):
        EightyNinety.append(RainfallInfoSorted[key])
    if (key >= 90 and key <= 100):
        NinetyHun.append(RainfallInfoSorted[key])

with open("rainfallfmt.txt", 'w') as file:
    print("[50-60 mm)", file = file)
    if (FiftySixty):
        for i in FiftySixty:
            print(i, file = file)
    print("[60-70 mm)", file = file)
    if (SixtySeventy):
        for i in SixtySeventy:
            print(i, file = file)
    print("[70-80 mm)", file = file)
    if (SeventyEighty):
        for i in SeventyEighty:
            print(i, file = file)
    print("[80-90 mm)", file = file)
    if (EightyNinety):
        for i in EightyNinety:
            print(i, file = file)
    print("[90-100 mm]", file = file)
    if (NinetyHun):
        for i in NinetyHun:
            print(i, file = file)