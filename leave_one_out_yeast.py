from termcolor import colored
import arff
from math import sqrt

TRAIN_FILE = 'trainData/yeast_train.arff'
TEST_FILE = 'testData/yeast_test.arff'
K = 3
K_LIST = [3, 5, 7]

PRINT_FLAG = 0


#from pro
def getPredictedClass(sliced_list):

    classname_dictionary = {}

    total_list_entry = 0

    for unitEntry in sliced_list:
        total_list_entry += 1
        if unitEntry[0] in classname_dictionary:
            current_count = classname_dictionary[unitEntry[0]][0]
            updated_count = current_count + 1

            classname_dictionary[unitEntry[0]] = [updated_count, unitEntry[2]]
            pass
        else:
            classname_dictionary[unitEntry[0]] = [1, unitEntry[2]]

    #print(classname_dictionary)
    for key in classname_dictionary:
        old_count = classname_dictionary[key][0]
        inverted_count = total_list_entry - old_count
        classname_dictionary[key] = [inverted_count, classname_dictionary[key][1]]

    #predicted_class = max(classname_dictionary, key= classname_dictionary.get)

    predicted_class = sorted(classname_dictionary, key=classname_dictionary.get, reverse=False)

    #print(classname_dictionary)

    #print(predicted_class)

    return predicted_class[0]


'''
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
'''

def calculateEuclideanDistance(point1, point2):

    sumOfSquare = 0

    for i in range(len(point1)):

        sumOfSquare += (point1[i] - point2[i])**2


    distance = sqrt(sumOfSquare)

    return distance

def getListFromArff(url):
    boroList = []

    row_serial = 1

    for row in arff.load(url):

        chotoList = []

        for attribute in row:
            chotoList.append(attribute)
        chotoList.append(row_serial)
        boroList.append(chotoList)

        row_serial += 1

    return boroList

def getIndividualResult(testData, trainList):

    global K
    global PRINT_FLAG

    distance_classname_list = []

    actual_class = testData[-2]

    for trainData in trainList:

        serial = trainData[-1]
        train_class = trainData[-2]
        distance = calculateEuclideanDistance(testData[:-2], trainData[:-2])

        distance_classname_list.append([train_class, distance, serial])

    #print(distance_classname_list)
    sorted_list = sorted(distance_classname_list, key= lambda x: x[1])
    #print(sorted_list)

    sliced_list_according_to_k = sorted_list[:K]

    #print(" Sliced List {}".format(sliced_list_according_to_k))

    predicted_class = getPredictedClass(sliced_list_according_to_k)

    if PRINT_FLAG == 1:


        print("Predicted class : {}	Actual class : {}".format(colored(predicted_class, 'red'), colored(actual_class, 'green')))


    if predicted_class == actual_class:
        return 1
    else:
        return 0

def solve_for_k():
    global K
    trainList = getListFromArff(TRAIN_FILE)
    #testList = getListFromArff(TEST_FILE)



    total_accurate = 0

    for i in range(len(trainList)):

        tempTrainList = trainList[:i] + trainList[i + 1:]

        temp_test_Data = trainList[i]

        total_accurate += getIndividualResult(testData=temp_test_Data, trainList=tempTrainList)

    print("Number of incorrectly classified instances for k = {} : {}".format(K, ((len(trainList)) - total_accurate)))

    return ((len(trainList)) - total_accurate)

def solve_for_optimum_k():
    trainList = getListFromArff(TRAIN_FILE)
    testList = getListFromArff(TEST_FILE)



    total_accurate = 0
    for testUnit in testList:

        total_accurate += getIndividualResult(testData=testUnit, trainList=trainList)
    print("Number of correctly classified instances : {}".format(total_accurate))
    print("Total number of instances : {}".format(len(testList)))
    print("Accuracy : {}".format(total_accurate/len(testList)))

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