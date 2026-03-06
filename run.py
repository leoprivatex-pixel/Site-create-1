from agents.crew import crew
from engine.auto_loop import AutoLoop

loop = AutoLoop(crew)

loop.run()