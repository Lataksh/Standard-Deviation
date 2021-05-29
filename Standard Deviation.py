import pandas as pd
import csv
import math
import statistics

with open("G:\Whitehat Junior\Python Projects\DataVisualization\class1.csv", newline='') as f:
    class2Data = csv.reader(f)
    data = list(class2Data)
    data.pop(0)
    # mean
    marks = 0
    totalEntries = len(data)
    for i in data:
        marks = marks + int(i[1])
    mean = marks / totalEntries
    
    print(mean)
    squaredData = []
    for i in data:
        subtractedData = float(i[1])-mean
        subtractedData = subtractedData**2
        squaredData.append(subtractedData)

    sumOfSquares = 0
    for i in squaredData:
        sumOfSquares += i

    subtractedSqrData = sumOfSquares / (len(data)-1)

    StandardDeviation = math.sqrt(subtractedSqrData)

    print("The standard deviation of the data given is " + StandardDeviation.__str__())

