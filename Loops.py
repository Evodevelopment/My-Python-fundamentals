## Focus on Readability of your Code :-)

#Udemy course outline

#enumarate

#Special   built in loop function - range():
print(range(0, 100))

for item in range (0, 100):
  print(item)
#I dont care for the varible name I just want to loop over the range:
for _ in range (100):
print(_)

#Iterable - list, dictionary, tuple, set, string


#Dictionaries have two main components: KEY and VALUE = k, v
for k, v in user_items:

  # Creating a dictionary to store information about a person
person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "city": "New York",
    "email": "john@example.com",
    "is_student": False,
    "skills": ["Python", "JavaScript", "SQL"],
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "zip_code": "10001"
    }
}

# Accessing values in the dictionary
print("First Name:", person["first_name"])
print("Age:", person["age"])
print("Skills:", person["skills"][0])  # Accessing the first skill
print("Street:", person["address"]["street"])

# Modifying values in the dictionary
person["age"] = 31
person["email"] = "johndoe@example.com"
person["skills"].append("HTML")
person["address"]["zip_code"] = "10002"

# Adding a new key-value pair
person["country"] = "USA"

# Deleting a key-value pair
del person["is_student"]

# Iterating through the dictionary
for key, value in person.items():
    print(key, ":", value)

###
#Loops
for item in "Zero to Mastery":
  print(item)

for item in (1,2,3,4,5):
  print(item)

for item in (1,2,3,4,5):
  print(item)
  print(item)
  print(item)

for item in (1,2,3,4,5):
  for x in [a, b, c]
    print(1, 'c')



#Logical operators
#if variable has certain logical value - 0 or 1, True of False, chceck == or != , then print this
is_magician = True
is_expert = False

if is_expert and is_magician:
  print("You are a master magician")

elif is_magician and not is_expert:
  print("at least you are getting there")

elif not is_magician:
  print("You need magic powers")

## Focus on Readability of your Code :-)
