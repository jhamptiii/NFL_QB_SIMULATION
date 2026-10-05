import random
class Quarterback:
    def __init__ (self, name, age, attributes, team):

        #basic information
        self.name = name
        self.age = age
        self.experience = 0
        self.potential = {}
        self.team = team

        #Core attributes  (hard coded all at 60 luck at 50, not yet or testing purpouses tho)
        self.endurance = attributes["endurance"]  #Injury resistance, recovery
        self.strength = attributes["strength"]   #throw power
        self.perception = attributes["perception"]    #awareness, decision making
        self.agility = attributes["agility"]      #speed  
        self.accuracy = attributes["accuracy"]      # accuracy   #later on, turn this into accuracy of short passes, medium, deep passes, under pressure accuracy, and throw on the run
        self.luck = attributes["luck"]       #influences every single action. a high luck player....just always seems to have things go their way. include critcal success and failures like in ffallout. when a critc success or failure from luck happens, make sure the player knows it was their luck skill's influence
        #player will pick skills, with a minimum of 40 and a maximum of 90
        #360 points to distribute through the character creation

        #hidden traits
        self.injury_proneness = max(0.5, min(random.gauss(1.0, 0.20), 1.5))  #0.50 = extremely durable, 1.00 = average, 1.50 = injury prone
        luck_modifier = 0.75 + (self.luck / 100) * 0.5  #this is factored into every formulaa, ints, breaking tackles, hail marys, etc
        self.clutch = max(0.50, min(random.gauss(1.0, 0.25), 1.50))



        #generate potential
        self.generate_potential()

        #calculate player skills
        self.calculate_skills()

        #calculate overall 
        self.calculate_overall()

        #calculate overall potential
        self.calculate_overall_potential()

    def generate_potential(self):

        self.potential["endurance"] = min(
            99,
            self.endurance + random.randint(5,25)  #enforces a 99
        )
        self.potential["strength"] = min(
            99,
            self.strength + random.randint(5,25)  #enforces a 99
        )
        self.potential["perception"] = min(
            99,
            self.perception + random.randint(5,25)  #enforces a 99
        )
        self.potential["agility"] = min(
            99,
            self.agility + random.randint(5,25)  #enforces a 99
        )
        self.potential["accuracy"] = min(
            99,
            self.accuracy + random.randint(5,25)  #enforces a 99
        )
        

    def calculate_overall(self):

        #overall stat           (redo this to be calulated off player skills instead of core attributes)
        self.overall = round(
            self.endurance * 0.17 +
            self.strength * 0.17 +
            self.perception * 0.22 +
            self.agility * 0.11 +
            self.accuracy * 0.33
        )

    def calculate_overall_potential(self):
                #overall potential stat           
        self.potential_overall = round(
            self.potential["endurance"] * 0.17 +
            self.potential["strength"] * 0.17 +
            self.potential["perception"] * 0.22 +
            self.potential["agility"] * 0.11 +
            self.potential["accuracy"] * 0.33
        )

    def calculate_skills(self):

        #player skills 
        self.throw_power = 40 + (self.strength * 0.6) + (self.endurance * 0.1)
        self.speed = self.agility + (self.endurance * 0.1)
        self.awareness = (self.perception * 0.80 + self.experience * 0.15 + self.luck * 0.05)
        self.decision_making = (self.perception * 0.65 + self.awareness * 0.20 + self.experience * 0.15)
        #self.short_pass_accuracy  # accuracy   #later on, turn this into accuracy of short passes, medium, deep passes, under pressure accuracy, and throw on the run
        #self.medium_pass_accuracy
        #self.deep_pass_accuracy
        #self.under_pressure_accuracy
        #self.on_the_run_accuracy
        #self.injury_resistance
        #self.injury_recovery
        






#throw_power
#accuracy       
#speed
#awareness
#decision_making
#strength
#injury_proneness   #secret stat
#luck

#i want the player to makea dice roll style atributes when making a character fallout style
# endurance - counters injury proneness and how fast you can heal from injuries, less likely to be injured
# strength - strength, throw power
# perception - desicion making, awareness
# agility -  speed 
# accuracy - accuracy
# luck - luck