#словарь для хранения выполненых ходов
flds = {"А0": None, "А1": None, "А2": None, "Б0": None, "Б1": None, "Б2": None, "В0": None, "В1": None, "В2": None}
#кто последний ходил
last_input = "0"
#списки подедных компинаций
w1,w2,w3,w4,w5,w6,w7,w8,all_wins = ([] for i in range(9))

def refrech_sets():
    """
списки надо обновить после каждого хода, чтобы синхронизировать с данными из словарю
    """
    global w1,w2,w3,w4,w5,w6,w7,w8,all_wins

    w1 = [flds["А0"], flds["А1"], flds["А2"]]
    w2 = [flds["Б0"], flds["Б1"], flds["Б2"]]
    w3 = [flds["В0"], flds["В1"], flds["В2"]]
    w4 = [flds["А0"], flds["Б0"], flds["В0"]]
    w5 = [flds["А1"], flds["Б1"], flds["В1"]]
    w6 = [flds["А2"], flds["Б2"], flds["В2"]]
    w7 = [flds["А0"], flds["Б1"], flds["В2"]]
    w8 = [flds["В0"], flds["Б1"], flds["А2"]]

    all_wins = [w1,w2,w3,w4,w5,w6,w7,w8] #все списки засунул в один, чтобы удобно пробежать по ним было

def none_remover(cell_to_check):
    """
При старте программы словарь ходов забит значениями None.
Эта функция подменяет None на пробел, чтобы не "ехало" форматирование игрового полю
    :param cell_to_check: ключ словаря для проверки содержимого
    :return: пробел, если начение None и игровой символ - если ход по этим координатам сделан
    """
    if cell_to_check is None:
        return " "
    else:
        return cell_to_check

def show_desk():
    """
отрисовывает игровое поле
    """
    print("\n"
          "   ", " | ", "А", " | ", "Б", " | ", "В", " | ", "\n"
          " - - | - - | - - | - - |\n"                                         
          " ", "0", " | ",none_remover(flds["А0"]), " | ", none_remover(flds["Б0"]), " | ", none_remover(flds["В0"]), " | ", "\n"
          " - - | - - | - - | - - |\n"                                                       
          " ", "1", " | ",none_remover(flds["А1"]), " | ", none_remover(flds["Б1"]), " | ", none_remover(flds["В1"]), " | ", "\n"
          " - - | - - | - - | - - |\n" 
          " ", "2", " | ",none_remover(flds["А2"]), " | ", none_remover(flds["Б2"]), " | ", none_remover(flds["В2"]), " | ", "\n"
          " - - | - - | - - | - - |\n"
          )


def check_winner(winner):
    """
проверяет появилась ли на игровом поле выигрышная комбинация
    :param winner: комбинации w1-w8
    :return: победителя, если есть или 0 если нет
    """
    if set(winner) == {"X"} or set(winner) == {"0"}:
        return winner[0]
    else:
        return 0


def check_move(cord,plyr):
    """
Проверяет координаты на легитимность: есть таковые или нет, если есть - был такой ход или нет.
    :param cord: введённые координаты для проверки
    :param plyr: текущий игрок
    :return: возвращает координаты после повторного ввода
    """
    global flds

    while cord not in flds.keys():
        cord = input(("Таких координат не существует, пожалуста введите верные координаты: ")).upper()
    while flds[cord] is not None:
        cord = (input(f"Такой ход уже был: Ходит {plyr} - введите координаты: ")).upper()
    return cord


def make_move(plyr):
    """
Собственно делает ход на игровом поле в зависимости от того, чей ход
    :param plyr: игрок, за которого надо сделать ход
    """
    global last_input

    coord = (input(f"Ходит {plyr} - введите координаты: ")).upper()
    checked = check_move(coord, plyr)
    flds[checked] = plyr
    last_input = plyr
    show_desk()


def the_game():
    """
Основнаю программа.
Воводит описание вначале игры
Крутит цикл, пока кто-то не выиграет или не закончатся ходы
    """
    print("Игра Крестики-Нолики.\n"
          "Чтобы сделать ход - введите координаты клетки и нажмите ВВОД.\n"
          "Пример ввода координат: А1 или а1")
    show_desk()
    global all_wins

    moves = 9

    while moves:

        if last_input == "0":
            make_move("X")
        else:
            make_move("0")

        refrech_sets()
        is_winner = list(map(check_winner, all_wins))

        if "X" in is_winner:
            print(f"Игра окончена на {10-moves} ходе - победили Крестики")
            break
        elif "0" in is_winner:
            print(f"Игра окончена на {10-moves} ходе - победили Нолики")
            break
        else:
            pass

        moves -= 1

        if not moves:
            print("Ходов не осталось. Игра окончена - победила Дружба!")
try:
    the_game()
except KeyboardInterrupt:
    print("\n\nВы завершили программу принудительно остановив её выполнение")