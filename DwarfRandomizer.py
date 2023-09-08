import random
from enum import Enum

def generateskilllist():
    points = 10
    skills = []

    while points > 0:

        # Determine proficiency level
        if(points >=5):
            proficiencyrand = random.randrange(1, 5, 1)
        elif(points == 1):
            proficiencyrand = 1
        else:
            proficiencyrand = random.randrange(1, points, 1)
        # Figure out which category we will select from and call the corresponding function
        categoryrand = random.random()

        # Crucial Skill Selected
        if categoryrand <= 0.25:
            skills.append(Proficiency(proficiencyrand).name.lower() + ' ' + selectcrucialskill().name.lower())
        # Labor Skill Selected
        elif categoryrand <=.50:
            skills.append(Proficiency(proficiencyrand).name.lower() + ' ' + selectlaborskill().name.lower())
        # Combat Skill Selected
        elif categoryrand <=.75:
            skills.append(Proficiency(proficiencyrand).name.lower() + ' ' + selectcombatskill().name.lower())
        # Other Skill Selected
        else:
            skills.append(Proficiency(proficiencyrand).name.lower() + ' ' + selectotherskill().name.lower())

        points = points - proficiencyrand
    return skills

def selectcrucialskill():
    skillToSelect = random.randrange(1, 23, 1)
    return CrucialSkill(skillToSelect)
def selectlaborskill():
    skillToSelect = random.randrange(1, 34, 1)
    return LaborSkill(skillToSelect)
def selectcombatskill():
    skillToSelect = random.randrange(1, 20, 1)
    return CombatSkill(skillToSelect)
def selectotherskill():
    skillToSelect = random.randrange(1, 44, 1)
    return OtherSkill(skillToSelect)



class OtherSkill(Enum):
    SWIMMER = 1
    WOUNDDRESSER = 2
    DIAGNOSTICIAN = 3
    SURGEON = 4
    BONEDOCTOR = 5
    SUTURER = 6
    CRUTCHWALKER = 7
    PERSUADER = 8
    NEGOTIATOR = 9
    LIAR = 10
    INTIMIDATOR = 11
    JUDGEOFINTENT = 12
    APPRAISER = 13
    ORGANIZER = 14
    RECORDKEEPER = 15
    CONVERSATIONALIST = 16
    COMEDIAN = 17
    FLATTERER = 18
    CONSOLER = 19
    PACIFIER = 20
    SCHEMER = 21
    STUDENT = 22
    CONCENTRATION = 23
    WORDSMITH = 24
    WRITER = 25
    POET = 26
    READER = 27
    SPEAKER = 28
    KEYBOARDIST = 29
    STRINGINSTRUMENTALIST = 30
    WINDINSTRUMENTALIST = 31
    PERCUSSIONIST = 32
    DANCER = 33
    CRITICALTHINKER = 34
    LOGICIAN = 35
    MATHEMATICIAN = 36
    ASTRONOMER = 37
    CHEMIST = 38
    GEOGRAPHER = 39
    OPTICSENGINEER = 40
    FLUIDENGINEER = 41
    LEADER = 42
    TACTICIAN = 43
    TEACHER = 44

class CombatSkill(Enum):
    AXEDWARF = 1
    SWORDSDWARF = 2
    MACEDWARF = 3
    HAMMERDWARF = 4
    SPEARDWARF = 5
    MARKSDWARF = 6
    SHIELDUSER = 7
    ARMORUSER = 8
    FIGHTER = 9
    ARCHER = 10
    WRESTLER = 11
    STRIKER = 12
    KICKER = 13
    BITER = 14
    DODGER = 15
    SIEGEENGINEER = 16
    SIEGEOPERATOR = 17
    MISCOBJECTUSER = 18
    DISCIPLINE = 19
    OBSERVER = 20

class LaborSkill(Enum):
    MECHANIC = 1
    POTTER = 2
    GLAZER = 3
    PAPERMAKER = 4
    BOOKBINDER = 5
    WAXWORKER = 6
    MILLER = 7
    THRESHER = 8
    HERBALIST = 9
    COOK = 10
    WEAVER = 11
    CLOTHIER = 12
    DYER = 13
    TRAPPER = 14
    AMBUSHER = 15
    TANNER = 16
    LEATHERWORKER = 17
    FISHDISSECTOR = 18
    ANIMALDISSECTOR = 19
    FISHCLEANER = 20
    CHEESEMAKER = 21
    MILKER = 22
    GELDER = 23
    SHEARER = 24
    SPINNER = 25
    PRESSER = 26
    BEEKEEPER = 27
    ANIMALTRAINER = 28
    ANIMALCARETAKER = 29
    SOAPER = 30
    LYEMAKER = 31
    POTASHMAKER = 32
    GLASSMAKER = 33
    PUMPOPERATOR = 34


class CrucialSkill(Enum):
    MINER = 1
    WOODCUTTER = 2
    CARPENTER = 3
    MASON = 4
    WEAPONSMITH = 5
    BOWYER = 6
    ARMORSMITH = 7
    BLACKSMITH = 8
    FURNACEOPERATOR = 9
    WOODBURNER = 10
    FISHERDWARF = 11
    BUTCHER = 12
    PLANTER = 13
    BREWER = 14
    GEMCUTTER = 15
    GEMSETTER = 16
    STONECUTTER = 17
    STONECARVER = 18
    ENGRAVER = 19
    METALCRAFTER = 20
    STONECRAFTER = 21
    WOODCRAFTER = 22
    BONECARVER = 23

class Proficiency(Enum):
    NOVICE = 1
    ADEQUATE = 2
    COMPETENT = 3
    SKILLED = 4
    PROFICIENT = 5


def main():
    print(list(generateskilllist()))

if __name__ == "__main__":
    main()





