import random

consonants = "bcdfghjklmnpqrstvwxyz"
vocals = "aeiou"

dump_file = "./usernames.txt"
num_usernames = 50

starting_vocal = True
username_length = 3

with open("schemas.txt", "r") as schema_file:
    schemas = schema_file.readlines()

usernames = []

valid_schemas = []
if starting_vocal:
    for schema in schemas:
        if schema[0] == "V":
            valid_schemas.append(schema)
        else:
            print(f"{schema} is not valid, skipping.")
else:
    valid_schemas = schemas

print("Starting username generation: ")
for i in range(num_usernames):
    username = ""
    schema = random.choice(valid_schemas)[:username_length]
    for j in range(username_length):
        if schema[j] == "V":
            username += random.choice(vocals)
        else:
            username += random.choice(consonants)
    usernames.append(username)
    print(username)