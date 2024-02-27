from random import choice
try:
    print('Добро пожаловать в игру "Камень-Ножницы-Бумага"')
    n = int(input('Введите сколько игр вы хотите сыграть : '))
    if n <= 0 :
        print ("Ошибка ввода")
    else :
        win = 0
        lose = 0
        draw = 0
        Stone = 0
        Paper = 0
        Clips = 0
        i = 0
        moves = {'камень': 0, 'ножницы': 0, 'бумага': 0}
        bot = ['камень', 'ножницы', 'бумага']
        while i != n:
            userMove = input('Ваш ход: ').lower()
            if userMove in moves:  # Проверка на точность хода пользователя
                if Stone> 2 and userMove == 'камень':  # если пользователь ходит больше 3 раз подряд,
                    print('Компьютер: бумага')  # то противник 100% будет его побеждать
                    print('Победа компьютера(Вы проиграли)')
                    moves['камень'] += 1
                    lose += 1
                elif Clips > 2 and userMove == 'ножницы':
                    print('Компьютер: камень')
                    print('Победа компьютера(Вы проиграли)')
                    moves['ножницы'] += 1
                    lose += 1
                elif Paper > 2 and userMove == 'бумага':
                    print('Компьютер: ножницы')
                    print('Победа компьютера(Вы проиграли)')
                    moves['бумага'] += 1
                    lose += 1
                else:
                    botMove = choice(bot)
                    if userMove == 'камень':
                        if botMove == 'бумага':
                            print('Компьютер: бумага')
                            print('Победа компьютера(Вы проиграли)')
                            lose += 1
                        elif botMove == 'ножницы':
                            print('Компьютер: ножницы')
                            print('Победа пользователя(Вы победили)')
                            win += 1
                        else:
                            print('Компьютер: камень')
                            print('Ничья')
                            draw += 1
                        moves['камень'] += 1
                        Stone += 1
                        Paper = 0
                        Clips = 0
                    elif userMove == 'бумага':
                        if botMove == 'ножницы':
                            print('Компьютер: ножницы')
                            print('Победа компьютера(Вы проиграли)')
                            lose += 1
                        elif botMove == 'камень':
                            print('Компьютер: камень')
                            print('Победа пользователя(Вы победили)')
                            win += 1
                        else:
                            print('Компьютер: бумага')
                            print('Ничья')
                            draw += 1
                        moves['бумага'] += 1
                        Stone = 0
                        Paper += 1
                        Clips = 0
                    elif userMove == 'ножницы':
                        if botMove == 'камень':
                            print('Компьютер: камень')
                            print('Победа компьютера(Вы проиграли)')
                            lose += 1
                        elif botMove == 'бумага':
                            print('Компьютер: бумага')
                            print('Победа пользователя(Вы победили)')
                            win += 1
                        else:
                            print('Компьютер: ножницы')
                            print('Ничья')
                            draw += 1
                        moves['ножницы'] += 1
                        Stone = 0
                        Paper = 0
                        Clips += 1
            else:  # если пользователь неправильно ходит
                print('Неверный ход')  # то игра будет продолжаться до тех пор, пока он не сыкрает n правильных ходов
                n += 1
            i += 1
        print('Статистика:')
        print(f" Победы: {win}   -    Поражения: {lose}   -   Ничьи: {draw}")
        for i in moves:
            print(f" {i}: {moves[i]}")
except ValueError:
    print("Ошибка, ты мог ввести цифры")
except:
    print("Ошибка")


