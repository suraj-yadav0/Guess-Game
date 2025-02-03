a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

a.append(9)
a.append("Suresh")


for i in a:
   try:
    if i < 5:
        print(i)
   except(ValueError, TypeError):
       pass