cat_attributes = {
    "intelligence": 25,
    "energy": 30,
    "weight": 15,
    # change the inital values above
}

print("Welcome to my Cat Game!")

# Take the user inputs for name and colour:
name = input("Enter name: ")
colour = input("What colour is your cat: ")
print("Here is " + name + "\'s Starting Attributes: ")
print(cat_attributes)
# ...
play = True
# start the while loop
while play:
    # Finish the string below
    option = input("What would you like to do? 1. Play with your Cat. 2. Train your Cat. 3. Show your Cat's Stats. 4. Feed your Cat. 5. Put your Cat to Sleep. 6. Exit Game: ")

    if option == '1':
        # change the cat's attributes here
        cat_attributes["energy"] -= 2
        cat_attributes["weight"] -= 1 
        print("Energy - 2. Weight - 1.")
        pass
    elif option == '2':
        cat_attributes["intelligence"] += 2
        cat_attributes["energy"] += 1
        print("")
        pass
    elif option == '3':
        print(cat_attributes)
    elif option == '4':
        cat_attributes["weight"] += 2
    elif option == '5':
        cat_attributes["intelligence"] += 1
        cat_attributes["energy"] += 5
    elif option == '6':
        play = False
        break
    else:
        pass

    # finish off the if statements below
    if cat_attributes["energy"] < 0 and cat_attributes["weight"] == 0:
        play = False
        print("Your Cat has Died.")
        break
    elif cat_attributes['energy'] < 2:
        print("You cannot train your cat or play with your cat")
        pass
    elif cat_attributes["weight"] > 50:
        print("You cannot feed your cat")
    
    else:
        pass
    