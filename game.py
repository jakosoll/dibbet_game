import time
from gibbet import Gibbet


def main():
    while True:
        print('Приветствуем в игре "Виселица"!\n'
              'Компьютер загадывает случайное слово, а вы должны его угадать')
        time.sleep(3)
        response = input('Готовы начать? Введите "Y" для начала или любой символ для выхода: ')
        time.sleep(1)
        if response.upper() != 'Y':
            print('До свидания!')
            time.sleep(1)
            break
        print('Переключите клавиатуру на русскую раскладку, игра начинается...')
        time.sleep(1)
        game = Gibbet()
        game.generate_word()
        while game.run_game:
            time.sleep(1)
            game.take_char(input('Попробуйте угадать букву: ', ))
        # if not game.win:
        #     game.get_right_word()
        response = input('Желатете сыграть еще раз? Введите "Y" для начала или любой символ для выхода: ')
        if response.upper() != 'Y':
            print('До свидания!')
            break


if __name__ == '__main__':
    main()
