from enums import GameState
from model import HangManModel
from view import HangManView


class HangManController:
    WELCOME_MESSAGE = "H A N G M A N"
    LETTER_NOT_IN_WORD_ERROR = "That letter doesn't appear in the word"
    ALREADY_GUESSED_MESSAGE = "You've already guessed this letter"
    INVALID_LETTER_ERROR = "Please enter a lowercase English letter"
    NO_SINGLE_LETTER_ERROR = "You should input a single letter"
    VALID_MENU_OPTIONS = ("play", "exit")

    def __init__(self, model: HangManModel, view: HangManView):
        self.model = model
        self.view = view

    def _show_welcome_message(self):
        self.view.show_message(self.WELCOME_MESSAGE)

    def start_game(self):
        self._show_welcome_message()

        menu_option = self._get_menu_option()

        while menu_option == "play":
            self._run_game_loop()

            if self.model.has_word_been_guessed():
                self.view.show_message("")
                self.view.show_message(self.model.get_guessed_word())
                self.view.show_message(GameState.GAME_WON.value)
            else:
                self.view.show_message(GameState.GAME_LOST.value)

            self.view.show_message("")
            menu_option = self._get_menu_option()

    def _get_menu_option(self) -> str:
        menu_option = self.view.prompt_for_menu_option()

        while menu_option not in self.VALID_MENU_OPTIONS:
            menu_option = self.view.prompt_for_menu_option()

        return menu_option

    def _run_game_loop(self):
        while (
            not self.model.has_word_been_guessed()
            and self.model.get_attempt_count() < self.model.MAX_ATTEMPTS
        ):

            self.view.show_message("")
            guessed_word = self.model.get_guessed_word()
            self.view.show_message(guessed_word)

            guessed_letter = self.view.prompt_for_letter()

            if not self.model.is_single_letter(guessed_letter):
                self.view.show_message(self.NO_SINGLE_LETTER_ERROR)

            if not self.model.is_valid_letter(guessed_letter):
                self.view.show_message(self.INVALID_LETTER_ERROR)
                continue

            if self.model.has_letter_already_been_guessed(guessed_letter):
                self.view.show_message(self.ALREADY_GUESSED_MESSAGE)
            else:
                letter_in_word = self.model.guess_letter(guessed_letter)

                if not letter_in_word:
                    self.view.show_message(self.LETTER_NOT_IN_WORD_ERROR)
                    self.model.increase_attempt_count()
