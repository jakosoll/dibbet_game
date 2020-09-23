import random
from typing import List
import time


class Gibbet:
    _word: str
    right_chars: List[str]
    error_chars: List[str]
    guess_word: str

    def __init__(self, errors=5):
        self.errors = errors
        self.right_chars = []
        self.error_chars = []
        self.run_game = True
        self.win = None
        self.guess_word = ''

    def generate_word(self):
        """Генерация слова, пока реализуем заглушку"""
        with open('WordsStockRus.txt', 'r', encoding='utf-8') as f:
            word_list = []
            for line in f.readlines():
                word_list.append(line.strip())
            self._word = random.choice(word_list)
            self.errors = len(self._word) + 1
        time.sleep(1)
        print('Компьютер сгенерировал слово')
        self.print_try_amount()

    def take_char(self, char: str):
        """
        Ввести букву
        Основная логика
        """
        if not self._check_char_lenght(char):
            time.sleep(1)
            print('Ошибка, вы ввели больше одного символа')
            return
        if char in self.right_chars or char in self.error_chars:
            print(f'Вы уже вводили {char}, введите другую букву')
            time.sleep(1)
            self.print_word()
            return
        if self._check_letter_in_word(char):
            print('Bingo!\n')
            print(f'Вы угадали букву {char}')
            self.right_chars.append(char)
            self.print_word()
            self._check_game()
        else:
            print('Извините, вы ошиблись')
            self.errors -= 1
            self._check_game()
            if not self.run_game:
                return
            self.error_chars.append(char)
            print(f'Вы вводили следушие буквы: \n{self.show_letters()}')
            self.print_word()
            self.print_try_amount()
            self._check_game()

    def print_try_amount(self):
        """Кол-во оставшихся попыток"""
        time.sleep(1)
        print(f"Осталось попыток: {self.errors} шт.")
        time.sleep(1)

    def print_word(self):
        """Показать открытые буквы,
        если буква скрыта вместо неё ставим подчёркивание или дефис"""
        self.guess_word = ''
        for char in self._word:
            if char in self.right_chars:
                self.guess_word += char
            else:
                self.guess_word += '-'
        time.sleep(1)
        print(f'Отгадываемое слово: => {self.guess_word}')

    def show_letters(self):
        """Показать буквы, которые клиент вводил"""
        time.sleep(1)
        return ', '.join(self.error_chars)

    def _check_letter_in_word(self, char: str):
        if self._word:
            return char.lower() in self._word

    def _check_game(self):
        if self.errors <= 0:
            self.run_game = False
            print('Вы проиграли')
            self._get_right_word()
        elif self.guess_word == self._word:
            self.run_game = False
            self.win = True
            print('Поздравляем, вы выиграли')

    def _get_right_word(self):
        print(f'Загаданное слово: "{self._word}"')

    def _check_char_lenght(self, char):
        return len(char) == 1
