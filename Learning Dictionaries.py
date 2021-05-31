# Learning About Dictionaries
from typing import KeysView


employees = {'name':'Jayaprakash','age':26}
for key,values in employees.items():
    print("Key Variables are: "+ key)

#Print List of Dictionary Key Values Pairs
print(list(employees.items()))
#Print Only key values in Dictionary
print(list(employees.keys()))
#printing only values in the Dictionary
print(list(employees.values()))
employees['name'] = "JayaKumar"
#Clears the Dictionary
employees.clear()
#Checking Wheather the Dictionary Contains any Data.
if ( len(list(employees.items()))==0 ):
    print("True")
# New way of Writing Dictionary
D = dict(name='Jayaprakash',age=26)
for i in D:
    print(D[i])
D.pop('name')
X= D.get('name')
print(X)