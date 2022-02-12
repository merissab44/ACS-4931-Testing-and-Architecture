# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math

grade_list = []

def print_grade_list():
    # Get the inputs from the user
    n_student = 5
    for _ in range(n_student):
        grade_list.append(int(input('Enter a number: ')))
    print(grade_list)
    return grade_list

def calculate_mean():
    mean = sum(grade_list) / len(grade_list)
    return mean

def calculate_standard_deviation():
    mean = calculate_mean()
    sd = 0 # standard deviation
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grade_list))
    return sd

def print_stat():
    print_grade_list()
    mean = calculate_mean()
    sd = calculate_standard_deviation()
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')
print_stat()
