# with open('exercise21.txt','r') as file:
#     all_text = file.read()
    
    
    
# print(all_text)



dict = {'Alisha': 100 , 'Amit': 200 , 'Rahul': 300 , 'Rohit': 400 , 'Raj': 500}



alishs = dict['Alisha']

# print(alishs)


dict['Alisha'] = 500

for pair in dict:
    print(pair, dict[pair])