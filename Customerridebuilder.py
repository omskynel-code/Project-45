print("WELCOME TO RIDE BUILDER")

print("Step1: Pick your vehicle")
print(" 1 - Bike")
print(" 2 - Car")
print()

choice = int(input("Enter 1 or 2:"))
print()

if choice == 1:
    print("Step 2: Pick your bike type")
    print(" 1 - Electric Bike")
    print(" 2 - Mountain Bike")
    print()

    bike_type = int(input("Enter 1 or 2:"))
    print()

    if bike_type == 1:
        print("You picked   : Electric Bike")
        print("Top speed    : 170 km/h")
        print("Best for     : Traveling across countries")
    else:
        print("You picked   : Mountain Bike")
        print("Top speed    : 90km/h")
        print("Best for     : Traveling across mountains")
elif choice == 2:
    print("Step 2: Pick your car type")
    print(" 1 - Nissan-2026")
    print(" 2 - Lambo")
    print()

    car_type = int(input("Enter 1 or 2: "))

    if car_type == 1:
        print("You picked   : Nissan-2026")
        print("Top speed    :  5 passengers")
        print("Best for     : Daily travels")
    else:
        print("You picked   : Mountain Bike")
        print("Top speed    : 4 passengers")
        print("Best for     : Flashy appearances ")

else:
    print("That was not a valid choice.")
    print("Please enter 1 for Bike or 2 for Car.")

print("==============================================")
print("      Your custom ride is ready!         ")  
print("      Enjoy the journey!                 ")   
print("==============================================")   
