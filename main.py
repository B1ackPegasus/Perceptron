import random


path_to_training_file = ""
path_to_file_test_data = ""
number_of_epoch = 0
learning_rate_alpha = 0


def user_provide_path():
    global path_to_training_file
    global path_to_file_test_data
    global learning_rate_alpha
    global number_of_epoch

    path_to_training_file = input("Provide path to the training file:")
    path_to_file_test_data = input("Provide path to file with test data:")
    learning_rate_alpha = float(input("Provide learning rate:"))
    number_of_epoch = int(input("Provide number of epochs:"))


LEN_FOR_WEIGHT_TRAINING = 0
LEN_OF_ONE_TRAINING_LINE = 0
array_of_arrays_of_training_data = []


def work_with_training_data():
    global LEN_FOR_WEIGHT_TRAINING
    global LEN_OF_ONE_TRAINING_LINE
    global array_of_arrays_of_training_data

    with open(path_to_training_file, "r") as file_train:
        lines = file_train.readlines()
        for line in lines:
            array_of_values_from_training_data = []
            list_of_items = line.split(",")
            list_of_items[len(list_of_items) - 1] = list_of_items[len(list_of_items) - 1].replace("\n", "")
            for i in range(0, len(list_of_items)-1):
                array_of_values_from_training_data.append(float(list_of_items[i]))
            array_of_values_from_training_data.append(list_of_items[len(list_of_items) - 1])
            array_of_arrays_of_training_data.append(array_of_values_from_training_data)

        LEN_FOR_WEIGHT_TRAINING = len(array_of_values_from_training_data) - 1
        LEN_OF_ONE_TRAINING_LINE = len(array_of_values_from_training_data)


TWO_CLASSES = []


def find_two_classes():
    global array_of_arrays_of_training_data
    global LEN_OF_ONE_TRAINING_LINE

    TWO_CLASSES.append(array_of_arrays_of_training_data[0][LEN_OF_ONE_TRAINING_LINE-1])
    for array in array_of_arrays_of_training_data:
        if array[LEN_OF_ONE_TRAINING_LINE-1] != TWO_CLASSES[0]:
            TWO_CLASSES.append(array[LEN_OF_ONE_TRAINING_LINE-1])
            break


def func_dict_class_number():
    global dict_class_number
    dict_class_number = {TWO_CLASSES[0]: 1, TWO_CLASSES[1]: 0}


dict_numb_class = {}


def func_dict_numb_class():
    global dict_numb_class
    dict_numb_class = {1: TWO_CLASSES[0], 0: TWO_CLASSES[1]}


def initialize_weights():
    i = 0
    while i < LEN_FOR_WEIGHT_TRAINING:
        WEIGHTS.append(0.001)
        i += 1


THRESHOLD = 1
Y = -1
dict_class_number = {}
WEIGHTS = []


def formula_training_data():
    global array_of_arrays_of_training_data
    global Y
    global dict_class_number
    global THRESHOLD
    global LEN_OF_ONE_TRAINING_LINE
    global learning_rate_alpha
    global WEIGHTS

    for array in array_of_arrays_of_training_data:
        result_w_x = 0
        for number_numer in range(0, len(array)-1):
            result_w_x += array[number_numer]*WEIGHTS[number_numer]
        if result_w_x >= THRESHOLD:
            Y = 1
        else:
            Y = 0

        for i in range(0, len(WEIGHTS)):
            WEIGHTS[i] = (WEIGHTS[i] + (dict_class_number[array[LEN_OF_ONE_TRAINING_LINE - 1]] - Y)
                          * learning_rate_alpha * array[i])

        THRESHOLD = THRESHOLD + (dict_class_number[array[LEN_OF_ONE_TRAINING_LINE - 1]] -
                                 Y) * learning_rate_alpha * (-1)


def shuffle():
    global array_of_arrays_of_training_data
    random.shuffle(array_of_arrays_of_training_data)


array_of_arrays_of_test_data = []


def working_with_test_data_file():
    global array_of_arrays_of_test_data

    with open(path_to_file_test_data, "r") as file_test_data:
        lines = file_test_data.readlines()
        for line in lines:
            array_of_values_from_test_data = []
            list_of_items = line.split(",")

            list_of_items[len(list_of_items) - 1] = list_of_items[len(list_of_items) - 1].replace("\n", "")
            for i in range(0, len(list_of_items)-1):
                array_of_values_from_test_data.append(float(list_of_items[i]))
            array_of_values_from_test_data.append(list_of_items[len(list_of_items) - 1])
            array_of_arrays_of_test_data.append(array_of_values_from_test_data)


TRUE_ANSWERS_TEST_DATA = 0


def formula_test_data():
    global array_of_arrays_of_test_data
    global LEN_OF_ONE_TRAINING_LINE
    global TRUE_ANSWERS_TEST_DATA
    global Y
    for array in array_of_arrays_of_test_data:
        result_w_x_test = 0
        for number_numer in range(0, len(array)-1):
            result_w_x_test += array[number_numer]*WEIGHTS[number_numer]
        if result_w_x_test >= THRESHOLD:
            Y = 1
        else:
            Y = 0
        if Y == dict_class_number[array[LEN_OF_ONE_TRAINING_LINE - 1]]:
            TRUE_ANSWERS_TEST_DATA += 1

    accuracy = TRUE_ANSWERS_TEST_DATA/len(array_of_arrays_of_test_data)
    print(f"Accuracy {accuracy*100}%")
    TRUE_ANSWERS_TEST_DATA = 0


array_numbers_from_user = []


def user_provide_date():
    global array_numbers_from_user
    array_numbers_from_user = []
    data_line = input("Provide a date to test: ")
    list_of_items_from_user = data_line.split(",")

    for i in range(0, len(list_of_items_from_user)):
        array_numbers_from_user.append(float(list_of_items_from_user[i]))


def user_data_find_answer():
    global array_numbers_from_user
    global WEIGHTS
    answer = 0
    for index_number in range(0, len(array_numbers_from_user)):
        answer += array_numbers_from_user[index_number]*WEIGHTS[index_number]
    if answer >= THRESHOLD:
        y = 1
    else:
        y = 0
    print(f"The answer is : {dict_numb_class[y]}")


def ask_user():
    work = True
    while work:
        user_choice = input("----------------------------\n"
                            "| Choose the option:       |\n"
                            "| 1 - Provide you own data |\n"
                            "| 2 - Exit                 |\n"
                            "----------------------------\n"
                            "Select: ")
        if user_choice == "1":
            user_provide_date()
            user_data_find_answer()
        elif user_choice == "2":
            work = False
        else:
            print("Incorrect input.")


user_provide_path()
work_with_training_data()
find_two_classes()
func_dict_class_number()
func_dict_numb_class()
initialize_weights()
working_with_test_data_file()


k = 0
while k < number_of_epoch:
    formula_training_data()
    shuffle()
    formula_test_data()
    k += 1


ask_user()
