import random 
from pathlib import Path
from obj.Dwarf import Dwarf
from obj.Skill import Skill
from enums.OtherSkill import OtherSkill
from enums.CombatSkill import CombatSkill
from enums.LaborSkill import LaborSkill
from enums.CrucialSkill import CrucialSkill


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
        proficiency = random.randrange(2, 6, 1)
    elif(points == 1):
        proficiency = 1
    else:
        proficiency = random.randrange(2, points+1, 1)
    
    #If the selected proficiency would end us with a single point left, round up
    #If its already at 5, round down to allow for a 2 selection on the next iteration
    
    if(points - proficiency == 1):
        if(proficiency == 5):
            proficiency -= 1
        else:
            proficiency += 1
        
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
    #Write the item list, The available materials change from embark to embark, but these are generic enough there shouldnt be issues. 
    #todo: This should probably get put into a constants class and handled less distinctly.
    textToWrite += "\t[ITEM:5:CLOTH:NONE:PLANT_MAT:GRASS_TAIL_PIG:THREAD]\n\t[ITEM:5:SEEDS:NONE:PLANT_MAT:MUSHROOM_HELMET_PLUMP:SEED]\n\t[ITEM:5:SEEDS:NONE:PLANT_MAT:GRASS_TAIL_PIG:SEED]\n\t[ITEM:5:SEEDS:NONE:PLANT_MAT:GRASS_WHEAT_CAVE:SEED]\n\t[ITEM:5:SEEDS:NONE:PLANT_MAT:POD_SWEET:SEED]\n\t[ITEM:5:SEEDS:NONE:PLANT_MAT:BUSH_QUARRY:SEED]\n\t[ITEM:5:SEEDS:NONE:PLANT_MAT:MUSHROOM_CUP_DIMPLE:SEED]\n\t[ITEM:1:ANVIL:NONE:INORGANIC:IRON]\n\t[ITEM:2:WEAPON:ITEM_WEAPON_AXE_BATTLE:INORGANIC:COPPER]\n\t[ITEM:2:WEAPON:ITEM_WEAPON_PICK:INORGANIC:COPPER]\n\t[ITEM:40:DRINK:NONE:PLANT_MAT:POD_SWEET:DRINK]\n\t[ITEM:20:DRINK:NONE:PLANT_MAT:GRASS_TAIL_PIG:DRINK]\n\t[ITEM:15:MEAT:NONE:CREATURE_MAT:GREEN_TREE_FROG:BRAIN]\n\t[ITEM:15:FISH:NONE:POND_TURTLE:MALE]\n\t[ITEM:15:PLANT:NONE:PLANT_MAT:MUSHROOM_HELMET_PLUMP:STRUCTURAL]\n\t[ITEM:5:BAG:NONE:PLANT_MAT:GRASS_TAIL_PIG:THREAD]\n\t[ITEM:5:THREAD:NONE:PLANT_MAT:GRASS_TAIL_PIG:THREAD]"
    writeFile(textToWrite, file)
     

if __name__ == "__main__":
    main()





