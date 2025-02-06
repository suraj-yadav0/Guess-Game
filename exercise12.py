# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.


# Lets create a list of numbers through a function


def fetch_list(hint_text, n):
     a = []
     print(hint_text)
     for i in range(n):
         a.append(int(input(f"Enter number {i+1}: ")))
        
     return a
 
 
 
# Now lets create a function that takes a list of numbers and returns a list of only the first and last elements of the given list


def get_first_and_last(a):
    b = []
    b.append(a[0])
    b.append(a[-1])
    
    return b




# main code

a = fetch_list("Enter the number of elements in the list:", 5)

b = get_first_and_last(a)


print(f"The first and last elements of the list are: {b}")
    
     
     