import os

def minimumMPG(): 
    while True:
        try:
            minMpg = float(input("Enter the minimum mpg ==> "))
            if minMpg < 0:
                print("Fuel economy given must be greater than 0")
            elif minMpg > 100:
                print("Fuel economy must be less than 100")
            else:
                return(minMpg) 
        except:
            print("You must enter a number for the fuel economy")

def getInputFile():
    while True:
        file = input("Enter the name of the input vehicle file ==> ")
        try:
            here = os.path.dirname(os.path.abspath(file))
            file = os.path.join(here, file)
            with open(file) as read_file:
                return[[data.strip() for data in line.strip().split("\t")] for line in read_file.readlines()]
        except:
            print("Could not open file", file)


def writeToFile(minMileage, fileData):
    while True:
        try:
            file = input("Enter the name of the file to output to ==> ")
            with open(file, "w") as writeFile:
                for data in fileData:
                    try:
                        if minMileage >= float(data[7]):
                            writeFile.write("{0:<40}{1:<40}{2:<40}{3:>10}\n".format(data[0],data[1],data[2],data[7]))
                    except:
                        print("Could not convert value", "{}".format(data[7]), "for vehicle", "{} {} {}".format(data[0],data[1],data[2]))
            break
        except IOError:
            print("There is an IO Error", file)

def main():
    minMileage = minimumMPG()
    print()
    fileData = getInputFile()[1:]
    print()
    writeToFile(minMileage,fileData)

if __name__ == "__main__":
    main()