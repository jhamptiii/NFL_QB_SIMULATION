import random
from player import Quarterback

TOTAL_POINTS = 400
MIN_ATTRIBUTE = 40
MAX_ATTRIBUTE = 90

def get_attribute(attribute_name, points_remaining, attributes_left):

    while True:

        print()
        print(f"Points remaining: {points_remaining}")
        print(f"Attributes remaining after this: {attributes_left - 1}")

        try:
            value = int(input(f"Choose {attribute_name} ({MIN_ATTRIBUTE}-{MAX_ATTRIBUTE}): "))

        except ValueError:
            print("Please enter a whole number.")
            continue

        if value < MIN_ATTRIBUTE:
            print(f"{attribute_name} cannot be lower than {MIN_ATTRIBUTE}.")

        elif value > MAX_ATTRIBUTE:
            print(f"{attribute_name} cannot be higher than {MAX_ATTRIBUTE}.")

        elif value > points_remaining - ((attributes_left - 1) * MIN_ATTRIBUTE):
            print(
                f"You don't have enough points for that. "
                f"You need to save at least "
                f"{(attributes_left - 1) * MIN_ATTRIBUTE} "
                f"points for the remaining attributes."
            )

        else:
            return value
        
def create_league():  #REDOTHIS needs to simulate previous year
    teams = {
        "Bills": {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "Dolphins" : {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "Patriots" : {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "Jets" : {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "Ravens" : {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "Bengals" : {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "Browns" : {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "Steelers" : {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "Texans": {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "Colts": {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "Jaguars": {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "Titans": {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "Broncos": {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "Chiefs": {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "Raiders": {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "Chargers": {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "Cowboys": {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "Giants": {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "Eagles": {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "Commanders": {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "Bears": {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "Lions": {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "Packers": {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "Vikings": {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "Falcons": {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "Panthers": {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "Saints": {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "Buccaneers": {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "Cardinals": {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "Rams": {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "FortyNiners": {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)},
        "Seahawks": {"OVO": random.randint(70,99), "OFF": random.randint(70,99), "DEF": random.randint(70,99)}
    }
    tempOVO = 99
    for row in teams:
        if teams[row]["OVO"] < tempOVO: 
            tempOVO = (teams[row]["OVO"])  
            firstPick = row

    return firstPick   #spits out first over all. player will always be first overall. if player overall is low first overall have a message say shocking reach 

def create_quarterback():

    print("=" * 50)
    print("        NFL QUARTERBACK CREATION")
    print("=" * 50)
    team = create_league()
    name = input("Enter quarterback name: ")

    while True:
        try:
            age = int(input("Enter quarterback age: "))

            if age < 18:
                print("Quarterback must be at least 18.")
            else:
                break

        except ValueError:
            print("Please enter a whole number.")

    attributes = {}

    points_remaining = TOTAL_POINTS

    core_attributes = [
        "endurance",
        "strength",
        "perception",
        "agility",
        "accuracy",
        "luck"
    ]

    for i, attribute in enumerate(core_attributes):

        attributes_left = len(core_attributes) - i

        value = get_attribute(
            attribute,
            points_remaining,
            attributes_left
        )

        attributes[attribute] = value
        points_remaining -= value

    print()
    print("=" * 50)
    print("CHARACTER CREATED")
    print("=" * 50)

    qb = Quarterback(name, age, attributes, team)
    
    print()
    print(f"Name:      {qb.name}")
    print(f"Age:       {qb.age}")

    print()
    print("CORE ATTRIBUTES")

    print(f"Endurance:  {qb.endurance}")
    print(f"Strength:   {qb.strength}")
    print(f"Perception: {qb.perception}")
    print(f"Agility:    {qb.agility}")
    print(f"Accuracy:   {qb.accuracy}")
    print(f"Luck:       {qb.luck}")

    print()
    print(f"Total Points: {sum(attributes.values())}")
    print(f"Overall:      {qb.overall}")

    print()
    print("CALCULATED SKILLS")

    print(f"Throw Power:      {qb.throw_power:.1f}")
    print(f"Speed:            {qb.speed:.1f}")
    print(f"Awareness:        {qb.awareness:.1f}")
    print(f"Clutch:  {qb.clutch:.1f}")
    print(f"Decision Making:  {qb.decision_making:.1f}")
    print(f"Injury Prone ( > 1 is bad):  {qb.injury_proneness:.1f}")

    print()
    print("ATTRIBUTE CAPS")

    print(f"Max Endurance:     {qb.potential["endurance"]:.1f}")
    print(f"Max Strength:      {qb.potential["strength"]:.1f}")
    print(f"Max Perception:    {qb.potential["perception"]:.1f}")
    print(f"Max Agility:      {qb.potential["agility"]:.1f}")
    print(f"Max Accuracy:      {qb.potential["accuracy"]:.1f}")

    print()
    print("OVERALL POTENTIAL")

    print(qb.potential_overall)

    print()
    print(f"SELECTED FIRST OVERALL BY THE  {qb.team}") 

def main():

    create_quarterback()
    
if __name__ == "__main__":
    main()