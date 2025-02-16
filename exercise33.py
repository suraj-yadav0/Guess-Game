# let us learn about Dictionaries

# That's how you create Dictionary
vegetable = {"tomato": 20.5, "potato": 12, "onion": 45, "cabbage": 50, "peas": 33, "carrot": 53}


# You Can also add elements in dictionary , one by one

vegetable["Baigan"] = 6

# You can print or access a single element like this
print(vegetable["tomato"])

# Not all the Values has to be same


vegetable["aalo"] = "shalu"

print(vegetable)

# Some Key Points..1. Keys must be unique, 2. If You try to fetch a key that doesnot exist , You will Get an Error
# I can either catch errors through Try and Catch Block or I can simply use a get method

print(vegetable.get("aalo", "kachalo"))
print(vegetable.get("samsosa","Nahi Mila Samosa"))

# Check if element is present in the Dictionary or not

print("lemon" in vegetable)


# Let us see the formatting of Strings

# Well I Know a Method of printing a number and a String together

a = 15
b = 17

print("The Value of a is " + str(a) + " and value of b is " + str(b))


# Well it works , but let us learn about .format method


print("The value of a is {} and the value of b is {}.".format(a,b))

# Now Let us create a Birthday Dictionary.

Birthday = {
    "Suraj Yadav": "07-08-2001",
    "Sanskriti Verma": "30-01-2001",
    "Sandhya DI": "19-01-1997",
    "Savita Di": "18-04-1994"
}

print("Welcome to the Birthday Dictionaries")

# Method 1: Using format() correctly
# print("We know the birthdays of: {}, {}, {}, {}".format(*Birthday.keys()))
#
# ques = input("Whose Birthday You want to Know : ")
#
# print("Birthday of " + ques + " is on " + str(Birthday[ques]))


#
# # Alternative methods:
#
# # Method 2: Using f-string (more readable)
# print(f"We know the birthdays of: {', '.join(Birthday.values())}")
#
# # Method 3: Direct string join
# print("We know the birthdays of: " + ", ".join(Birthday.values()))