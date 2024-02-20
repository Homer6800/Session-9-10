import random

fruits = ["apple", "Banana", "Cherry"]
print(fruits)
fruits.append("date")

fruits.extend(["Elderberry", "fig", "grape"])
fruits += ["honeydew", "Kiwi", "lemon"]

print(fruits)

while True:
    fruit = random.choice(fruits)
    like = input(f"Do you like {fruit}? (yes/no) ")
    if like.lower() == "yes":
        new_fruit = input(f"Name another fruit to add: ")
    elif like.lower() == "no":
        print(f"removing {fruit} from the list. ")
        fruits.remove(fruit)
    elif like.lower() == "stop":
        break

with open("fruits.txt", "w") as fd:
    for fruit in fruits:
        fd.write(fruit + "\n")
