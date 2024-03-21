import json

#define a python dictionary

person={
    "name": "John", 
    "age":"30",
    "city":"New York",
    "hasChildren":False, 
    "titles":["engineer","programmer"]}

print(type(person))

person_json=json.dumps(person)
print(type(person_json))
print(person_json)

person_json=json.dumps(person,indent=4,separators=(";"," = "), sort_keys=True)

print(person_json)

print("========================================Practice 2 - create json file=========================================")

person2={
    "name": "John", 
    "age":"30",
    "city":"New York",
    "hasChildren":False, 
    "titles":["engineer","programmer"]}

with open("C:/Users/12816/Python/python_fundamentals_ik_live/week_3/person_2.json","w") as file:
    json.dump(person2,file)    

print("========================================Practice 3 - Deserialize json to python dictionary=========================================")    

with open("C:/Users/12816/Python/python_fundamentals_ik_live/week_3/person_2.json","r") as file:
    loaded_person=json.load(file)
    print(type(loaded_person))
    print(loaded_person)
    print(loaded_person["name"])