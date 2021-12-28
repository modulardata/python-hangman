
class HangManView:
    @staticmethod
    def prompt_for_letter() -> str:
        return input("Input a letter: ")

    @staticmethod
    def show_message(message):
        print(message)

    @staticmethod
    def prompt_for_menu_option() -> str:
        return input('Type "play" to play the game, "exit" to quit: ')