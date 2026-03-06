import os

class ProjectLoader:

    def __init__(self, path):

        self.path = path

    def load_files(self):

        files = []

        for root, dirs, filenames in os.walk(self.path):

            for f in filenames:

                path = os.path.join(root, f)

                try:

                    with open(path, "r", encoding="utf-8", errors="ignore") as file:

                        content = file.read()

                    files.append({
                        "path": path,
                        "content": content
                    })

                except:
                    pass

        return files