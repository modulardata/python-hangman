import enum


class GameState(enum.Enum):
    GAME_LOST = "You lost!"
    GAME_WON = "You guessed the word!\nYou survived!"
    NEXT_STAGE = "Thanks for playing!\nWe'll see how well you did in the " \
                 "next stage"
