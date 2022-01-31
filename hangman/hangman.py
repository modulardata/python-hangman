from controller import HangManController
from model import HangManModel
from view import HangManView

model = HangManModel()
view = HangManView()
controller = HangManController(model, view)

controller.start_game()
