import os

class SkillLoader:

    def __init__(self, skills_dir="skills"):
        self.skills_dir = skills_dir

    def load_skills(self):

        skills = []

        for file in os.listdir(self.skills_dir):

            if file.endswith(".md"):

                path = os.path.join(self.skills_dir, file)

                with open(path, "r", encoding="utf-8") as f:

                    skills.append(f.read())

        return skills