# from collections import Counter
#
# sandwiches = ["ham", "cheese", "roast beef", "ham", "cheese", "roast beef", "ham"]
#
# c = Counter(sandwiches)
#
# print(c)\

# Let's create the Birthday Bash



from collections import  Counter
import json

# Birthday = {
#     "Suraj Yadav": {
#         "date" : 7,
#         "month" : "August",
#         "year"  : 2001
#     },
#     "Sanskriti Verma":  {
#         "date" : 30,
#         "month" : "January",
#         "year"  : 2001
#     },
#     "Sandhya DI":  {
#         "date" : 19,
#         "month" : "January",
#         "year"  : 1997
#     },
#     "Savita Di":  {
#         "date" : 18,
#         "month" : "April",
#         "year"  : 1994
#     }
# }
#
# with open("birthday.json", 'w') as f:
#     json.dump(Birthday,f)




with open('birthday.json', 'r') as f:
    birthdays = json.load(f)



# Extract months from the birthday data
months = [info['month'] for info in birthdays.values()]

# Count occurrences of each month
month_counts = Counter(months)

# Convert to dictionary and format
result = dict(month_counts)

# Print formatted result
print(json.dumps(result, indent=4))


