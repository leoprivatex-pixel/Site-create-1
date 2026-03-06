class AutoLoop:

    def __init__(self, crew):

        self.crew = crew

    def run(self):

        while True:

            print("Analyzing project")

            self.crew.kickoff()

            print("Cycle complete")