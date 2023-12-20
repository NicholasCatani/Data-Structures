######################
### Data Structures #2


### Write a python program to find the maximum of three numbers in a list.

def max_of_three(lst):
    if len(lst) < 3:
        return "The list must contain at least three numbers."
    return max(lst[:3])


### Write a python program to multiply all the numbers in a list.

def multiply_list(lst):
    result = 1
    for number in lst:
        result *= number
    return result


### Write a python program to reverse a list.

def reverse_list_in_place(lst):
    lst.reverse()
    return lst


### Write a python function to check whether a number falls within a given range of list.

def is_number_in_range(number, start, end):
    return start <= number <= end


### Write a python function that accepts a string and counts the number of upper and lower case letters.

def count_upper_lower(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count


### Write a python function that takes a list and returns a new list with distinct
### elements from the first list.

def distinct_elements(lst):
    distinct_list = list(set(lst))
    return distinct_list


### Apply all system defined functions on a given list.

sample = [3, 5, 1, 4, 1, 9, 2, 6, 5, 3, 1, 8, 7]
sorted_sample = sorted(sample)
max_value = max(sample)
min_value = min(sample)
total = sum(sample)
distinct_list = list(set(sample))


### Write a program to convert a list into a dictionary.

sample = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}
keys_to_extract = ["name", "salary"]
extraction = {key: sample[key] for key in keys_to_extract}


### Write a program to create a dictionary by extrating the keys from a given dictionary.

samp_dictionary = {"a":1, "b":2, "c":3}
new = {key: None for key in samp_dictionary.keys()}


### Write a program to get the key of a minimum value from the following dictionary.

sample = {
    "Physics": 82,
    "Math": 65,
    "History": 75
}
minimum = min(sample, key=sample.get)

### Write a program to sort dictionary by values - descending scores.

sample = {
    "Physics": 82,
    "Math": 65,
    "History": 75,
    "Chemistry": 89,
    "GK": 50
}
sorted_sample = dict(sorted(sample.items(), key=lambda item[1], revense=True))



