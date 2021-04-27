
import json
import sys
import csv


def count_contractions(pressure_data):
    """
    Count the number of contractions for a pressure curve

    :param pressure_data: a list of pressure points
    :return: The total number of contractions
    """
    Peek1 = False
    Low1 = False
    Peek2 = False
    count = 0
    for row in pressure_data:
        kPa = float(row[1])
        if kPa > 95 and Peek1 == False:
            Peek1 = True
        if kPa < 85 and Peek1 == True and Low1 == False:
            Low1 = True
        if kPa > 95 and Low1 == True and Peek1 == True:
            Peek2 = True
        if Peek1 == True and Low1 == True and Peek2 == True:
            count = count + 1
            Peek1 = False
            Low1 = False
            Peek2 = False

    return count


def contractions_per_sec(pressure_data):
    """
    Calculate the mean contractions / secs for a pressure curve

    :param pressure_data: a list of pressure points
    :return: The mean frequency of contraction / secs
    """
    Peek1 = False
    Low1 = False
    Peek2 = False
    count = 0
    start = 0
    end = 0
    timings = []

    for row in pressure_data:
        kPa = float(row[1])
        if kPa > 95 and Peek1 == False:
            Peek1 = True
            start = int(row[0])
        if kPa < 85 and Peek1 == True and Low1 == False:
            Low1 = True
        if kPa > 95 and Low1 == True and Peek1 == True:
            Peek2 = True
            end = int(row[0])
        if Peek1 == True and Low1 == True and Peek2 == True:
            count = count + 1
            Peek1 = False
            Low1 = False
            Peek2 = False
            timings.append(end - start)

    if count != 0:
        total = count / (sum(timings) / 1000)
    else:
        total = 0
    return total


"""
    The update function for Json is not updating the file right now but the function will be in the same way.
    I have updated the Json file with the pressure_3.csv for displaying the data.

"""


def updatePressureJson(pressure_data, contractionCount, contractionPerSec):
    pressureJson = {
        "pressure_points": [],
        "count_contractions": contractionCount,
        "contractions_per_sec": contractionPerSec
    }
    for row in pressure_data:
        ms = float(row[0])
        kPa = float(row[1])
        pressureJson["pressure_points"].append({
            "ms": ms,
            "pressure": kPa
        })

    data = json.dumps(pressureJson)
    with open("dashboard/src/pressure.json", "w") as jsonfile:
        jsonfile.write(data)


def main():
    pressure_file = sys.argv[1]
    # n contraction count & #s is contraction / s
    n = 0
    s = 0
    with open(pressure_file, 'rt')as f:
        # start from second line
        next(f)
        data = csv.reader(f)
        n = count_contractions(data)

    with open(pressure_file, 'rt')as f:
        # start from second line "
        next(f)
        data = csv.reader(f)
        s = contractions_per_sec(data)

    with open(pressure_file, 'rt')as f:
        next(f)
        data = csv.reader(f)
        updatePressureJson(data, n, s)

    print("---")
    print("For {}:".format(pressure_file))
    print("* Number of contraction = {}".format(n))
    print("* Contraction / s = {}".format(n))

    return 0


if __name__ == '__main__':
    sys.exit(main())
