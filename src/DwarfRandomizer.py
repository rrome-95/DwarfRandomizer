import random 
from enum import Enum
from pathlib import Path

def generateDwarves():
    dwarves = []
    while len(dwarves) < 7:
        points = 10
        dwarf = Dwarf([])
        while points > 0:
            skillname = generateSkill(dwarf.skills).name
            proficiency = generateProficiency(points)
            dwarf.skills.append(Skill(skillname, proficiency))
            points -= proficiency
            
        dwarves.append(dwarf)
        
    return dwarves
    
#Generates a number within the legal range of proficiencies based on points.
def generateProficiency(points):
    proficiency = 0
    if(points >=5):
        proficiency = random.randrange(1, 6, 1)
    elif(points == 1):
        proficiency = 1
    else:
        proficiency = random.randrange(1, points+1, 1)
        
    return proficiency
    

#Returns a random skill from one of the 4 categories
def generateSkill(skills):
    def selectcrucialskill():
        skillToSelect = random.randrange(1, 24, 1)
        return CrucialSkill(skillToSelect)
    def selectlaborskill():
        skillToSelect = random.randrange(1, 35, 1)
        return LaborSkill(skillToSelect)
    def selectcombatskill():
        skillToSelect = random.randrange(1, 21, 1)
        return CombatSkill(skillToSelect)
    def selectotherskill():
        skillToSelect = random.randrange(1, 47, 1)
        return OtherSkill(skillToSelect)

    # Figure out which category we will select from.
    categoryrand = random.random()
    existingSkills  = []
    for skill in skills:
        existingSkills.append(skill.skillname)
        
    while True:
        if categoryrand <= 0.25:
            skillFound = selectcrucialskill()
        elif categoryrand <=.50:
            skillFound = selectlaborskill()
        elif categoryrand <=.75:
            skillFound = selectcombatskill()
        else:
            skillFound = selectotherskill()

        if (existingSkills.count(skillFound) == 0):
            return skillFound
            
    return 
    
            
            

class OtherSkill(Enum):
    SWIMMING = 1
    DRESS_WOUNDS = 2
    DIAGNOSE = 3
    SURGERY = 4
    SET_BONE = 5
    SUTURE = 6
    CRUTCH_WALK = 7
    PERSUASION = 8
    NEGOTIATION = 9
    LYING = 10
    INTIMIDATION = 11
    JUDGING_INTENT = 12
    APPRAISAL = 13
    ORGANIZATION = 14
    RECORD_KEEPING = 15
    CONVERSATION = 16
    COMEDY = 17
    FLATTERY = 18
    CONSOLE = 19
    PACIFY = 20
    INTRIGUE = 21
    KNOWLEDGE_ACQUISITION = 22
    CONCENTRATION = 23
    WRITING = 24
    PROSE = 25
    POETRY = 26
    READING = 27
    SPEAKING = 28
    PLAY_KEYBOARD_INSTRUMENT = 29
    PLAY_STRINGED_INSTRUMENT = 30
    PLAY_WIND_INSTRUMENT = 31
    PLAY_PERCUSSION_INSRTUMENT = 32
    DANCER = 33
    CRITICAL_THINKING = 34
    LOGIC = 35
    MATHEMATICS = 36
    ASTRONOMY = 37
    CHEMISTRY = 38
    GEOGRAPHY = 39
    OPTICS_ENGINEER = 40
    FLUID_ENGINEER = 41
    LEADERSHIP = 42
    MILITARY_TACTICS = 43
    TEACHING = 44
    SING = 45
    MAKE_MUSIC = 46

class CombatSkill(Enum):
    AXE = 1
    SWORD = 2
    MACE = 3
    HAMMER = 4
    SPEAR = 5
    CROSSBOW = 6
    SHIELD = 7
    ARMOR = 8
    MELEE_COMBAT = 9
    RANGED_COMBAT = 10
    WRESTLING = 11
    GRASP_STRIKE = 12
    STANCE_STRIKE = 13
    BITE = 14
    DODGING = 15
    SIEGECRAFT = 16
    SIEGEOPERATE = 17
    MISC_WEAPON = 18
    DISCIPLINE = 19
    SITUATIONAL_AWARENESS = 20

class LaborSkill(Enum):
    MECHANICS = 1
    POTTERY = 2
    GLAZING = 3
    PAPERMAKING = 4
    BOOKBINDING = 5
    WAX_WORKING = 6
    MILLING = 7
    PROCESSPLANTS = 8
    HERBALISM = 9
    COOK = 10
    WEAVING = 11
    CLOTHESMAKING = 12
    DYER = 13
    TRAPPING = 14
    SNEAK = 15
    TANNER = 16
    LEATHERWORK = 17
    DISSECT_FISH = 18
    DISSECT_VERMIN = 19
    PROCESSFISH = 20
    CHEESEMAKING = 21
    MILK = 22
    GELD = 23
    SHEARING = 24
    SPINNING = 25
    PRESSING = 26
    BEEKEEPING = 27
    ANIMALTRAIN = 28
    ANIMALCARE = 29
    SOAP_MAKING = 30
    LYE_MAKING = 31
    POTASH_MAKING = 32
    GLASSMAKER = 33
    OPERATE_PUMP = 34

class CrucialSkill(Enum):
    MINING = 1
    WOODCUTTING = 2
    CARPENTRY = 3
    MASONRY = 4
    FORGE_WEAPON = 5
    BOWYER = 6
    FORGE_ARMOR = 7
    FORGE_FURNITURE = 8
    SMELT = 9
    WOOD_BURNING = 10
    FISH = 11
    BUTCHER = 12
    PLANT = 13
    BREWING = 14
    CUTGEM = 15
    ENCRUSTGEM = 16
    CUT_STONE = 17
    CARVE_STONE = 18
    ENGRAVE_STONE = 19
    METALCRAFT = 20
    STONECRAFT = 21
    WOODCRAFT = 22
    BONECARVE = 23


class Dwarf:
    def __init__(self, skills):
        self.skills = skills

    def getSkillsOutput(self,number):
        ret = ""
        for skill in self.skills:
            ret += "\t[SKILL:" + str(number) + ":" + skill.skillname + ":" + str(skill.proficiency) + "]\n"
        return ret;
            
    
class Skill:
    def __init__(self, name, proficiency):
        self.skillname = name
        self.proficiency = proficiency
    
    
    
def getFile():
    data_folder = Path(r'C:\Program Files (x86)\Steam\steamapps\common\Dwarf Fortress\prefs')
    file_to_open = data_folder / "embark_profiles.txt"
    f = open(file_to_open, 'a')
    return f
    
def writeFile(text, file):
    #file.write("\n")
    file.write(text)
    file.close()
    

def main():
    file = getFile()
    dwarves = generateDwarves()
    ind = 1
    textToWrite = "[PROFILE]\n\t[TITLE:test]\n"
    for dwarf in dwarves:
        textToWrite += (dwarf.getSkillsOutput(ind))
        ind += 1
    writeFile(textToWrite, file)
     

if __name__ == "__main__":
    main()





