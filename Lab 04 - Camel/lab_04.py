import random
i = 0
camel_tiredness = 0
miles_traveled = 0
natives_traveled = -20
canteen = 3
thirst = 0
nativesBehind = miles_traveled - natives_traveled
fullSpeed = random.randrange(10, 21)
moderateSpeed = random.randrange(5, 13)

print("""Welcome to School!
You have stolen a classmate to make your way across the great Overlake Campus.
    The Principle wants his student back and is chasing you down! Survive your
    campus trek and out run the Principle. Beware of expulsion!""")

while True:
    print("""
    A. Drink from your canteen.
    B. Ahead moderate speed.
    C. Ahead full speed.
    D. Stop for the night.
    E. Status check.
    Q. Quit.""")
    userInput = input("What is your choice?")
    if userInput.lower() == "Q":
        break

    elif userInput.lower() == "E":
        print("Miles traveled: ", miles_traveled)
        print("Drinks in canteen: ", canteen)
        print("Your student has ", camel_tiredness, "amount of fatigue.")
        print("The principle is ", natives_traveled, "miles behind you.")

    elif userInput.lower() == "D":
        camel_tiredness *= 0
        print("Your student feels refreshed and happy his fatigue is now ", camel_tiredness)
        natives_traveled += i in range(7, 15)

    elif userInput.lower() == "c":
        miles_traveled += fullSpeed
        thirst += 1
        print("You traveled ", fullSpeed, "miles!")
        camel_tiredness += i in range(1, 4)
        natives_traveled += i in range(7, 15)

    elif userInput.lower() == "b":
        print("You traveled ", moderateSpeed, "miles!")
        miles_traveled += moderateSpeed
        thirst += 1
        camel_tiredness += 1
        natives_traveled += i in range(7, 15)

    elif userInput.lower() == "a":
        if canteen == 0:
            print("You're out of water.")
        else:
            canteen -= 1
            thirst *= 0
            print("You have ", canteen, "drinks left and you are no longer thirsty.")

    else:
        print("invalid")
        break

    if nativesBehind <= 15:
        print("The Principle is drawing near!")
    if miles_traveled >= 200 and not True:
        print("You made it across the Overlake campus, you win!")
        break
    if natives_traveled >= miles_traveled:
        print("The Principle caught and expelled you.")
        print("You're life is over!")
        break
    if thirst > 4 and thirst <= 6 and not True:
        print("You are thirsty")
    if thirst > 6:
        print("You died of dehydration!")
        break
    if camel_tiredness > 5 and camel_tiredness <= 8 and not True:
        print("Your student is getting tired.")
    if camel_tiredness > 8:
        print("Your student is dead. Wow you suck.")
        break