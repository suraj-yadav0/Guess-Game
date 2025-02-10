list = []
list2 = []
list3 = []

with open('one.txt','r') as file_one:
    
    
    list = file_one.read()
    list = list.split()
    
    
with open('other.txt','r') as file_two:
    list2 = file_two.read()
    list2 = list2.split()
    


for i in list:
    for j in list2:
        if i == j:
            list3.append(i)
            
            
            
print(list3)