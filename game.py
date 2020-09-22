import time
from gibbet import Gibbet


def main():
    while True:
        print('Приветствуем в игре "Виселица"\n'
              'Компьютер загадывает случайное слово,\n'
              'а вы должны его угадать')
        time.sleep(1)
        response = input('Готовы начать? Введите "Y" для начала или любой символ для выхода: ')
        time.sleep(1)
        if response.upper() != 'Y':
            print('До свидания!')
            time.sleep(1)
            break
        time.sleep(1)
        print('Переключите клавиатуру на русскую раскладку, игра начинается...')
        time.sleep(1)
        game = Gibbet()
        game.generate_word()
        while game.run_game:
            game.take_letter(input('Попробуйте угадать букву: '))
        response = input('Желатете сыграть еще раз?Введите "Y" для начала или любой символ для выхода: ')
        if response.upper() != 'Y':
            print('До свидания!')
            break


if __name__ == '__main__':
    main()
