import random
from typing import List


class Gibbet:
    _word: str
    right_chars: List[str]
    error_chars: List[str]
    end_game: bool

    def __init__(self, errors=5):
        self.errors = errors
        self.right_chars = []
        self.error_chars = []
        self.run_game = True
        self.win = None

    def generate_word(self):
        """Генерация слова, пока реализуем заглушку"""
        with open('WordsStockRus.txt', 'r') as f:
            word_list = []
            for line in f.readlines():
                word_list.append(line.strip())
            self._word = random.choice(word_list)
            self.errors = len(self._word) + 1
        print('Компьютер сгенерировал слово')
        self.print_try_amount()

    def take_letter(self, char):
        """Ввести букву (попытка)"""
        if self._check_letter_in_word(char):
            print('Bingo!\n')
            self.right_chars.append(char)
            self.print_word()
        else:
            print('Извините, вы ошиблись')
            self.errors -= 1
            self.error_chars.append(char)
            self.print_try_amount()

    def print_try_amount(self):
        """Кол-во оставшихся попыток"""
        print(f"Осталось попыток: {self.errors} шт.")

    def print_word(self):
        """Показать открытые буквы,
        если буква скрыта вместо неё ставим подчёркивание или дефис"""
        word: str = ''
        for char in self._word:
            if char in self.right_chars:
                word += char
            else:
                word += '-'
        print(word)

    def show_letters(self):
        """Показать буквы, которые клиент вводил"""

        return ', '.join(self.error_chars)  # TODO: огранизовть проверку и вывод введеных букв

    def _check_letter_in_word(self, char: str):
        if self._word:
            return char.lower() in self._word

    def _check_game(self):
        if self.errors <= 0:
            self.run_game = False
            print('Извините, вы проиграли')
        elif len(self.right_chars) == len(self._word):
            self.run_game = False
            self.win = True
            print('Поздравляем, вы выиграли')
