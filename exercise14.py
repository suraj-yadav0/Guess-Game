# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.


def remove_duplicates(a):
    return list(set(a))




a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



print(remove_duplicates(a))