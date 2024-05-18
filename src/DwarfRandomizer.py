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





