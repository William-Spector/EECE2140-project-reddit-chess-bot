import json

filename = input("What is the name of your json file? ")

outfile = open(filename+".json", 'w')

a = True

b = {"Docstring":"This object created using genjson by William Spector"}

while a:
    att = input("What is the name of the attribute?")
    val = input("What is the value of the object?")
    b[att] = val
    a = True if (input('Would you like to add more attributes? ') in ['y', 'Y', 'yes', 'Yes', 'YES']) else False
    
if (input('Would you like to remove the docstring? ') in ['y', 'Y', 'yes', 'Yes', 'YES']):
    del b["Docstring"]

outfile.write(json.dumps(b))