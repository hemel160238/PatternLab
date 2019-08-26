from nltk.corpus import stopwords
from collections import Counter

all_words_set = []

list_containing_all_article = []

n_of_train_data = 18


def getUnitCalculation(c, a, d, n):
    return (c+a)/(d+n)

def formatArticle(article):

    splitted_article = article.split('\n')
    name = splitted_article[0].lower()
    category = splitted_article[1]

    word_list = []

    for i in range(2, len(article.split('\n'))):
        for word in (splitted_article[i].split()):

            if word.endswith('.'):
                word_list.append(word[:-1].lower())

            else:
                word_list.append(word.lower())

    filtered_word_list = [word for word in word_list if word not in stopwords.words('english')]

    #print([category, filtered_word_list])
    return [category.lower(), filtered_word_list, name]

def getProcessedArticleList():

    global list_containing_all_article
    global n_of_train_data

    print(" Number of Train Data is : {}".format(n_of_train_data))
    filepath = "bioCorpus.txt"

    crs = open(filepath, "r")
    whole_corpus = crs.read()

    article_list = []
    formatted_article_list = []

    for unit_articles in whole_corpus.split("\n\n"):
        if(len(unit_articles) > 0):
            article_list.append(unit_articles)

    for article in article_list:
        formatted_article_list.append(formatArticle(article))

    list_containing_all_article = formatted_article_list

    return formatted_article_list[:n_of_train_data]


def makeTopicWordDictionary(article_list):

    topic_word_dict = {}
    topic_count_dict = {}
    total_article = len(article_list)

    for article in article_list:

        article_category = article[0]
        article_words = article[1]

        if article_category in topic_word_dict:

            existing_words = topic_word_dict[article_category]
            added_words = existing_words + article_words
            topic_word_dict[article_category] = added_words

            existing_count = topic_count_dict[article_category]
            added_count = existing_count + 1
            topic_count_dict[article_category] = added_count

        else:

            topic_word_dict[article_category] = article_words
            topic_count_dict[article_category] = 1

    for topic in topic_count_dict:
        current_count = topic_count_dict[topic]
        topic_count_dict[topic] = current_count/total_article

    return [topic_word_dict, topic_count_dict]

def makeTamimLikeDictionary(topic_dict):

    new_dict = {}

    for topic in topic_dict:
        words_array = topic_dict[topic]
        word_count_dict = dict(Counter(words_array))
        new_dict[topic] = word_count_dict

    return new_dict

def calculateProbability(frequency_dict, topic_ratio, topic_dict, article):
    #frequency_dict is dictionary of dictionary with word frequency over topic
    #topic_ratio is dictionary containing topic probability

    global all_words_set


    given_topic_name = article[0]
    given_topic_word_list = article[1]
    given_article_name = [2]


    a = 1
    d = len(all_words_set)

    topic_prediction_list = []

    for topic in topic_ratio:

        p = 1

        n = len(topic_dict[topic])

        for word in given_topic_word_list:
            unit_probability = 1

            if word in all_words_set:
                if word in frequency_dict[topic]:

                    count = frequency_dict[topic][word]

                    unit_probability = getUnitCalculation(count, a, d, n)

                else:
                    unit_probability = getUnitCalculation(0, a, d, n)

            p *= unit_probability

        p *= topic_ratio[topic]

        topic_prediction_list.append([topic, p])

    sorted_list = sorted(topic_prediction_list, key= lambda x: x[1], reverse=True)

    verdict = ''
    if(sorted_list[0][0] == article[0]):
        verdict = 'Right'
    else:
        verdict = 'Wrong'

    print("{}.    Prediction: {}    {}".format(article[2], sorted_list[0][0], verdict))

    for i in range(1, len(sorted_list)):
        print("{} : {}".format(sorted_list[i][0], sorted_list[i][1]), end=" ")
    print("\n")

    pass

def prepareAllUniqueWordsList(topic_dict):
    global all_words_set
    temp_list = []

    for topic in topic_dict:
        temp_list += topic_dict[topic]

    all_words_set = set(temp_list)

    return all_words_set

def runTest():

    print(len(list_containing_all_article))
    pass


#input data



article_list = getProcessedArticleList()
topic_dict__topic_ratio = makeTopicWordDictionary(article_list)

# topic_dict have form
topic_dict = topic_dict__topic_ratio[0]
topic_ratio = topic_dict__topic_ratio[1]


#Preparing ALl Words List from topic_dict
prepareAllUniqueWordsList(topic_dict)


#Test Article
article = ['government',['american', 'lawyer,', 'u.s', 'representative,', 'social', 'activist', 'leader', "women's", 'movement', 'abzug', 'joined', 'leading', 'feminists', 'gloria', 'steinem', 'betty', 'friedan', 'found', 'national', "women's", 'political', 'caucus', 'french', 'general', 'statesman', 'led', 'free', 'french', 'forces', 'world', 'war', 'ii', 'later', 'founded', 'french', 'fifth', 'republic', 'served', 'first', 'president', 'british', 'conservative', 'politician,', 'writer', 'aristocrat', 'twice', 'served', 'prime', 'minister', 'played', 'central', 'role', 'creation', 'modern', 'conservative', 'party,', 'defining', 'policies', 'broad', 'outreach', 'burmese', 'opposition', 'politician', 'chairperson', 'national', 'league', 'democracy', 'burma', 'american', 'politician', 'civil', 'rights', 'leader', 'us', 'representative', 'georgias', 'fifth', 'congressional', 'district', 'dean', 'georgia', 'congressional', 'delegation', 'french', 'politician', 'president', 'poitou', 'charentes', 'regional', 'council,', 'former', 'member', 'national', 'assembly,', 'former', 'government', 'minister,', 'prominent', 'member', 'french', 'socialist', 'party'],'Bella Abzug ']

#Make Tamim Like Dict
frequency_dict = makeTamimLikeDictionary(topic_dict)
#calculateProbability(frequency_dict, topic_ratio, topic_dict, article)


for i in range(n_of_train_data, len(list_containing_all_article)):
    print("+-------------------------------------------------------+")
    calculateProbability(frequency_dict, topic_ratio, topic_dict, list_containing_all_article[i])





