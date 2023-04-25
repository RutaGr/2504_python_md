from db import Db

db = Db()

while True:
    to_do = input(
        "What you want to do? (insert = i, delete = d, show = s, update = u, quit = q?)")

    if (to_do == "i"):
        to_do = input("To do: ")
        db.insert(to_do,)
        break

    elif (to_do == "d"):
        print("Which to do do you want to delete?: ")
        db.select()
        id = input("Id: ")
        db.delete(id)

        break

    elif (to_do == "s"):
        db.select()
        break

    elif (to_do == "u"):

        print("Which to do do you want to update?")
        db.select()
        condition = input("Id:")
        value = input("To do: ")

        db.update(condition, value)

        break

    elif (to_do == "q"):
        break
