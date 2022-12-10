#Create a new class for pets
class Pet:

    #Initialize class with name and type
    def __init__(self, name, type):
        self.name = name
        self.type = type

#Create a list to store the pets
pets = []

#Function to add a pet
def add_pet():
    name = input("Enter the pet's name: ")
    type = input("Enter the type of pet: ")
    pet = Pet(name, type)
    pets.append(pet)
    print("Pet added successfully!")

#Function to list all pets
def list_pets():
    print("List of Pets:")
    for pet in pets:
        print(pet.name + " (" + pet.type + ")")

#Function to remove a pet
def remove_pet():
    name = input("Enter the pet's name: ")
    for pet in pets:
        if pet.name == name:
            pets.remove(pet)
            print("Pet removed successfully!")
            break
        else:
            print("Pet not found!")

#Function to search for a pet
def search_pet():
    name = input("Enter the pet's name: ")
    for pet in pets:
        if pet.name == name:
            print("Pet found:")
            print(pet.name + " (" + pet.type + ")")
            break
        else:
            print("Pet not found!")

#Main function
def main():
    while True:
        print("Pet Store Management System")
        print("1. Add Pet")
        print("2. List Pets")
        print("3. Remove Pet")
        print("4. Search Pet")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_pet()
        elif choice == 2:
            list_pets()
        elif choice == 3:
            remove_pet()
        elif choice == 4:
            search_pet()
        elif choice == 5:
            break
        else:
            print("Invalid choice!")

#Call main function
if __name__ == "__main__":
    main()