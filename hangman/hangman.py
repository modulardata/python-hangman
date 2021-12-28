from Hangman.task.hangman.controller import HangManController
from Hangman.task.hangman.model import HangManModel
from Hangman.task.hangman.view import HangManView

model = HangManModel()
view = HangManView()
controller = HangManController(model, view)

controller.start_game()
