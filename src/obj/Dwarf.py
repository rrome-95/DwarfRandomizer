class Dwarf:
    def __init__(self, skills):
        self.skills = skills

    def getSkillsOutput(self,number):
        ret = ""
        for skill in self.skills:
            ret += "\t[SKILL:" + str(number) + ":" + skill.skillname + ":" + str(skill.proficiency) + "]\n"
        return ret;