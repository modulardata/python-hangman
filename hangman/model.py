import random
from typing import List


class HangManModel:
    _POSSIBLE_WORDS = ["python", "java", "kotlin", "javascript"]
    _HINT_LENGTH = 3
    MAX_ATTEMPTS = 8

    def __init__(self):
        self._word = random.choice(self._POSSIBLE_WORDS)
        self._guessed_word = self._generate_empty_guessed_word_template()
        self._attempt_count = 0
        self._guessed_letters = set()

    def has_word_been_guessed(self) -> bool:
        return self._guessed_word == self._word

    def _generate_empty_guessed_word_template(self):
        return "-" * len(self._word)

    def get_guessed_word(self):
        return self._guessed_word

    def get_attempt_count(self):
        return self._attempt_count

    def increase_attempt_count(self):
        self._attempt_count += 1

    def _find_indices_of_letter_in_word(self, letter: str) -> List[int]:
        return [index for index, char in enumerate(self._word)
                   if letter == char]

    def _add_letter_at_indices(self, letter: str, indices: List[int]) -> str:
        guessed_word_list = list(self._guessed_word)

        for index in indices:
            guessed_word_list[index] = letter

        return "".join(guessed_word_list)

    def _update_guessed_letters(self, letter: str):
        if letter not in self._guessed_letters:
            self._guessed_letters.add(letter)

    @staticmethod
    def is_single_letter(letter: str) -> bool:
        return len(letter) == 1

    def is_valid_letter(self, letter: str) -> bool:
        is_letter = letter.isalpha()
        is_lowercase = letter.islower()
        is_single_character = self.is_single_letter(letter)

        return is_single_character and is_lowercase and is_letter

    def guess_letter(self, letter: str) -> bool:
        self._update_guessed_letters(letter)

        relevant_indices = self._find_indices_of_letter_in_word(letter)

        if len(relevant_indices) <= 0 or self._guessed_word == self._word:
            return len(relevant_indices) > 0
        self._guessed_word = self._add_letter_at_indices(
            letter,
            relevant_indices
        )
        return True

    def has_letter_already_been_guessed(self, letter: str) -> bool:
        return letter in self._guessed_letters

    def has_max_attempts_been_reached(self):
        return self._attempt_count == self.MAX_ATTEMPTS
