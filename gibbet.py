class Gibbet:
    def __init__(self, errors=3):
        self.errors = errors

    def generate_word(self):
        pass

    def take_letter(self, letter):
        pass

    def __len__(self):
        """Кол-во оставшихся попыток"""
        pass

    def __str__(self):
        """Показать открытые буквы,
        если буква скрыта вместо неё ставим подчёркивание или дефис"""
        pass

    def show_letters(self):
        """Показать буквы, которые клиент вводил"""
        pass