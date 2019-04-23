
# coding: utf-8

# Here goes the imports
import csv
import matplotlib.pyplot as plt

# Let's read the data as a list
print("Reading the document...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Let's check how many rows do we have
print("Number of rows:")
print(len(data_list))

# Printing the first row of data_list to check if it worked.
print("Row 0: ")
print(data_list[0])
# It's the data header, so we can identify the columns.

# Printing the second row of data_list, it should contain some data
print("Row 1: ")
print(data_list[1])

input("Press Enter to continue...")
# TASK 1
# TODO: Print the first 20 rows using a loop to identify the data.
print("\n\nTASK 1: Printing the first 20 samples")

# Let's change the data_list to remove the header from it.
data_list = data_list[1:]

# We can access the features through index
# E.g. sample[6] to print gender or sample[-2]
sample_20_rows = data_list[0:20]
print(sample_20_rows)

input("Press Enter to continue...")
# TASK 2
# TODO: Print the `gender` of the first 20 rows
print("\nTASK 2: Printing the genders of the first 20 samples")
print([row[6] for row in sample_20_rows])

# Cool! We can get the rows(samples) iterating with a for and the columns(features) by index.
# But it's still hard to get a column in a list. Example: List with all genders

input("Press Enter to continue...")
# TASK 3
# TODO: Create a function to add the columns(features) of a list in another list in the same order
def column_to_list(data, index):
    """ get all data column with specified index
    Args 
        data: list of list (All data)
        index: column index (An Integer)
    Return
        a list of elements from data
    """
    column_list = []
    # Tip: You can use a for to iterate over the samples, get the feature by index and append into a list
    column_list = [row[index] for row in data]
    return column_list


# Let's check with the genders if it's working (only the first 20)
print("\nTASK 3: Printing the list of genders of the first 20 samples")
print(column_to_list(data_list, -2)[:20])

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(column_to_list(data_list, -2)) is list, "TASK 3: Wrong type returned. It should return a list."
assert len(column_to_list(data_list, -2)) == 1551505, "TASK 3: Wrong lenght returned."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TASK 3: The list doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we know how to access the features, let's count how many Males and Females the dataset have
# TASK 4
# TODO: Count each gender. You should not use a function to do that.
male = 0
female = 0

male = len([gender for gender in column_to_list(data_list, -2) if gender == 'Male'])
female = len([gender for gender in column_to_list(data_list, -2) if gender == 'Female'])

# Checking the result
print("\nTASK 4: Printing how many males and females we found")
print("Male: ", male, "\nFemale: ", female)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert male == 935854 and female == 298784, "TASK 4: Count doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Why don't we creeate a function to do that?
# TASK 5
# TODO: Create a function to count the genders. Return a list
# Should return a list with [count_male, counf_female] (e.g., [10, 15] means 10 Males, 15 Females)
def count_gender(data_list):
    """ Count how many Male and Female inside given list
    Args 
        data_list: list of string that contains Gender
    Return
        Return a list that contains the result (first position corresponding to Male and second Female)
    """
    male = len([gender for gender in column_to_list(data_list, -2) if gender == 'Male'])
    female = len([gender for gender in column_to_list(data_list, -2) if gender == 'Female'])
    return [male, female]


print("\nTASK 5: Printing result of count_gender")
print(count_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(count_gender(data_list)) is list, "TASK 5: Wrong type returned. It should return a list."
assert len(count_gender(data_list)) == 2, "TASK 5: Wrong lenght returned."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TASK 5: Returning wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we can count the users, which gender use it the most?
# TASK 6
# TODO: Create a function to get the most popular gender and print the gender as string.
# We expect to see "Male", "Female" or "Equal" as answer.
def most_popular_gender(data_list):
    """ Return most popular Gender
    Args 
        data: list of Genders
    Return
        Return most popular gender as a String
    """
    answer = ""
    male, female = count_gender(data_list)
    if male > female:
        answer = "Male"
    elif female > male:
        answer = "Female"
    else:
        answer = "Equal"

    return answer


print("\nTASK 6: Which one is the most popular gender?")
print("Most popular gender is: ", most_popular_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(most_popular_gender(data_list)) is str, "TASK 6: Wrong type returned. It should return a string."
assert most_popular_gender(data_list) == "Male", "TASK 6: Returning wrong result!"
# -----------------------------------------------------

# If it's everything running as expected, check this graph!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Gender')
plt.xticks(y_pos, types)
plt.title('Quantity by Gender')
plt.show(block=True)

# Clear Plot
plt.gcf().clear()

input("Press Enter to continue...")
# TASK 7
# TODO: Plot a similar graph for user_types. Make sure the legend is correct.

def generic_counter(data_list, column_index, list_values_to_count):
    """ Generic Version of count gender (Using column_to_list function)
    Args 
        data_list: list of list (All data)
        column_index: column index to search values and count (An Integer)
        list_values_to_count: a list with which values to count on given column index of data
    Return
        return a list of integers with result, for exemple: list of values to count: ["column1", "column2"] => result: [10, 20]
        whitch 10 corresponde to column1 and 20 to column2
    """
    result = []
    for value in list_values_to_count:
        result.append(len([gender for gender in column_to_list(data_list, column_index) if gender == value]))
    return result

print("\nTASK 7: Check the chart!")
user_type_list = column_to_list(data_list, -3)
user_types = ["Customer", "Subscriber"]
quantity = generic_counter(data_list, -3, user_types)
print("Quantity Result: ", quantity)
y_pos = list(range(len(user_types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('User Types')
plt.xticks(y_pos, user_types)
plt.title('Quantity by User Types')
plt.show(block=True)

# Clear Plot
plt.gcf().clear()

input("Press Enter to continue...")
# TASK 8
# TODO: Answer the following question
male, female = count_gender(data_list)
print("\nTASK 8: Why the following condition is False?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "It is False because there is a lot of empty string on Gender column."
print("Answer:", answer)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert answer != "Type your answer here.", "TASK 8: Write your own answer!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Let's work with the trip_duration now. We cant get some values from it.
# TASK 9
# TODO: Find the Minimum, Maximum, Mean and Median trip duration.
# You should not use ready functions to do that, like max() or min().
def get_max_min(data_list, flag):
    """ get max or min value from list of integers, depending on flag value
    Args 
        data: a list of integers (All data)
        flag: option to perform: "min" or "max" (String)
    Return
        Returns min or max values as integer
    """
    result = int(data_list[0])
    if flag == "max":
        for data in data_list:
            if int(data) >= result:
                result = int(data)
    elif flag == "min":   
        for data in data_list:
            if int(data) < result:
                result = int(data)
    return result

def sum_values(data_list):
    """ Sum all values on a list
    Args 
        data: list of integers
    Return
        Sum result as integer
    """
    result = 0
    for value in data_list:
        result += int(value)
    return result

def get_len(data_list):
    """ Get the lenght of given list
    Args 
        data_list: list (any type of elements)
    Return
        return length as integer
    """
    result = 0
    for _ in data_list:
        result += 1
    return result

def sort_list(tail, ordered_list=[]):
    """ Sort a list of integers recursively (Works on Small Lists)
    Args 
        tail: list of elements to sort
        ordered_list: innitialy empty (Will be the list that contains result)
    Return
        return ordered list
    """
    if get_len(tail) > 0:
        minimum = get_max_min(tail, "min")       
        ordered_list.append(minimum)
        tail.remove(minimum)
        return sort_list(tail, ordered_list)
    else:
        return ordered_list

def get_median(data_list):
    """ Calculates Median of given list
    Args 
        data_list: list of elements to calculate Median
    Return
        return median result as integer or float 
    """
    data_lenght = get_len(data_list)
    # ordered_list = sort_list(data_list) => that function works but is taking too long to process, so I used built in function for that
    ordered_list = sorted(data_list)

    if data_lenght % 2 == 0:
        return (int(ordered_list[(data_lenght // 2) - 1]) + int(ordered_list[(data_lenght // 2)])) / 2
    else:
        return int(ordered_list[data_lenght // 2])

trip_duration_list = [int(x) for x in column_to_list(data_list, 2)] # Return as a list of integers
min_trip = get_max_min(trip_duration_list, "min")
max_trip = get_max_min(trip_duration_list, "max")
mean_trip = sum_values(trip_duration_list)/get_len(trip_duration_list)


median_trip = get_median(trip_duration_list)


print("\nTASK 9: Printing the min, max, mean and median")
print("Min: ", min_trip, "Max: ", max_trip, "Mean: ", mean_trip, "Median: ", median_trip)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert round(min_trip) == 60, "TASK 9: min_trip with wrong result!"
assert round(max_trip) == 86338, "TASK 9: max_trip with wrong result!"
assert round(mean_trip) == 940, "TASK 9: mean_trip with wrong result!"
assert round(median_trip) == 670, "TASK 9: median_trip with wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 10
# Gender is easy because usually only have a few options. How about start_stations? How many options does it have?
# TODO: Check types how many start_stations do we have using set()
user_types = set()
start_stations_list = column_to_list(data_list, 3)
for station in start_stations_list:
    user_types.add(station)

print("\nTASK 10: Printing start stations:")
print(len(user_types))
print(user_types)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert len(user_types) == 582, "TASK 10: Wrong len of start stations."
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 11
# Go back and make sure you documented your functions. Explain the input, output and what it do. Example:
# def new_function(param1: int, param2: str) -> list:
"""
Example function with annotations.
Args:
    param1: The first parameter.
    param2: The second parameter.
Returns:
    List of X values

"""

input("Press Enter to continue...")
# TASK 12 - Challenge! (Optional)
# TODO: Create a function to count user types without hardcoding the types
# so we can use this function with a different kind of data.
print("Will you face it?")
answer = "yes"

def count_items(column_list):
    item_types = []
    count_items = []
    # Creating a list of distinct items
    for item in column_list:
        if item not in item_types:
            item_types.append(item)
    
    for value in item_types:
        count_items.append(len([gender for gender in column_list if gender == value]))

    return item_types, count_items


if answer == "yes":
    # ------------ DO NOT CHANGE ANY CODE HERE ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTASK 11: Printing results for count_items()")
    print("Types:", types, "Counts:", counts)
    assert len(types) == 3, "TASK 11: There are 3 types of gender!"
    assert sum(counts) == 1551505, "TASK 11: Returning wrong result!"
    # -----------------------------------------------------