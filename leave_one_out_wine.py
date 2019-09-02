from termcolor import colored
import arff
from math import sqrt

TRAIN_FILE = 'trainData/wine_train.arff'
TEST_FILE = 'testData/wine_test.arff'
K = 7
K_LIST = [3, 5, 7]

PRINT_FLAG = 0

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
    global PRINT_FLAG

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

    class_sum = 0
    for unit in sliced_list_according_to_k:
        class_sum += unit[0]

    predicted_value = class_sum/K

    #print("Predicted value : {0:.6f}\t\t	Actual value : {0:.6f}".format(colored(predicted_value, 'red'), colored(actual_class, 'cyan')))
    #print("Predicted value : {0:.6f}\t\t	Actual value : {0:.6f}".format(predicted_value, actual_class))
    #print("Predicted value : {0:.6f}".format(predicted_value), end="	")
    #print("Actual value : {0:.6f}".format(actual_class))

    if(PRINT_FLAG == 1):
        print("Predicted value : {0:.6f}".format(predicted_value), end="	")
        print("Actual value : {0:.6f}".format(actual_class))



    return abs(predicted_value - actual_class)

def solve_for_k():
    trainList = getListFromArff(TRAIN_FILE)

    #trainList = trainList[10]

    total_error = 0

    for i in range(len(trainList)):

        tempTrainList = trainList[:i] + trainList[i+1 :]

        temp_test_Data = trainList[i]
        #print("Temp Test Data : {} and now list is  {}".format(temp_test_Data, len(tempTrainList)))

        total_error += getIndividualResult(testData=temp_test_Data, trainList=tempTrainList)



    print("Mean absolute error for k = {} : {}".format(K, total_error/(len(trainList))))

    return total_error/(len(trainList))

def solve_for_optimum_k():
    trainList = getListFromArff(TRAIN_FILE)
    testList = getListFromArff(TEST_FILE)

    getIndividualResult(testData=testList[3], trainList=trainList)


    total_error = 0
    for testUnit in testList:

        total_error += getIndividualResult(testData=testUnit, trainList=trainList)
    print("Mean absolute error : {}".format(total_error/len(testList)))
    print("Total number of instances : {}".format(len(testList)))


def solve():

    global K_LIST
    global K
    global PRINT_FLAG

    print(K_LIST)

    k_and_error_list = []

    for k in K_LIST:
        K = k

        error = solve_for_k()

        k_and_error_list.append([k, error])

    sorted_list = sorted(k_and_error_list, key=lambda x: x[1])

    optimum_k = sorted_list[0][0]

    print("Best k value : {}".format(optimum_k))

    K = optimum_k

    PRINT_FLAG = 1
    solve_for_optimum_k()

    pass

solve()
