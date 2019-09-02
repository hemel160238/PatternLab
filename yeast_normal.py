import arff
from math import sqrt
from termcolor import colored

TRAIN_FILE = 'trainData/yeast_train.arff'
TEST_FILE = 'testData/yeast_test.arff'
K = 3

def getPredictedClass(sliced_list):

    classname_dictionary = {}

    for unitEntry in sliced_list:
        if unitEntry[0] in classname_dictionary:
            classname_dictionary[unitEntry[0]] += 1
            pass
        else:
            classname_dictionary[unitEntry[0]] = 1

    #print(classname_dictionary)
    predicted_class = max(classname_dictionary, key= classname_dictionary.get)

    #print(predicted_class)

    return predicted_class

def calculateEuclideanDistance(point1, point2):

    sumOfSquare = 0

    for i in range(len(point1)):

        sumOfSquare += (point1[i] - point2[i])**2


    distance = sqrt(sumOfSquare)

    return distance

def getListFromArff(url):
    #global TRAIN_FILE

    #url = TRAIN_FILE

    boroList = []

    for row in arff.load(url):

        chotoList = []

        for attribute in row:
            chotoList.append(attribute)

        boroList.append(chotoList)

    #print(len(boroList))

    return boroList

def getIndividualResult(testData, trainList):

    global K

    distance_classname_list = []

    actual_class = testData[-1]

    for trainData in trainList:

        train_class = trainData[-1]
        distance = calculateEuclideanDistance(testData[:-1], trainData[:-1])

        distance_classname_list.append([train_class, distance])

    #print(distance_classname_list)
    sorted_list = sorted(distance_classname_list, key= lambda x: x[1])
    #print(sorted_list)

    sliced_list_according_to_k = sorted_list[:K]

    #print(" Sliced List {}".format(sliced_list_according_to_k))

    predicted_class = getPredictedClass(sliced_list_according_to_k)

    print("Predicted class : {}	Actual class : {}".format(colored(predicted_class, 'red'), colored(actual_class, 'green')))


    if predicted_class == actual_class:
        return 1
    else:
        return 0

def solve():
    trainList = getListFromArff(TRAIN_FILE)
    testList = getListFromArff(TEST_FILE)



    total_accurate = 0
    for testUnit in testList:

        total_accurate += getIndividualResult(testData=testUnit, trainList=trainList)
    print("Number of correctly classified instances : {}".format(total_accurate))
    print("Total number of instances : {}".format(len(testList)))
    print("Accuracy : {}".format(total_accurate/len(testList)))

solve()