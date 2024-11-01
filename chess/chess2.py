
'''
   mode = 'WhoAttack' - вернёт список некоторых объектов фигур, которые бьют фигуру Figure.
   mode = 'common' - Покажет, как ходит фигура Figure
   '''

import random


def convertmove(m):
    if m == 'exit': raise EndOfTheGame
    return (7 - (ord(m[0].upper()) - ord('A')), int(m[1]) - 1)


def generator(num, times):
    for i in range(times):
        yield num


class Team():
    side = 0
    enemy = 0


class White(Team):
    side = -1
    enemy = 1


class Black(Team):
    side = 1
    enemy = -1


class Battlefield():
    def __init__(self):
        self.field = [[Space() for i in range(8)] for j in range(8)]
        self.field[0] = [Rook(Black), Knight(Black), Goose(Black),
                         Queen(Black), King(Black),
                         Goose(Black), Knight(Black), Rook(Black)]
        self.field[1] = [Mouse(Black)] * 8
        self.field[-1] = [Rook(White), Knight(White), Goose(White),
                          Queen(White), King(White), Goose(White),
                          Knight(White), Rook(White)]
        self.field[-2] = [Mouse(White)] * 8

        for i, line in enumerate(self.field):
            for j, figure in enumerate(line):
                figure.x = i
                figure.y = j

    def __repr__(self):
        s = ''
        for i, line in enumerate(self.field):
            s += str(i + 1) + '| '
            for fig in line:
                if fig.__class__ == Space:
                    s += '__ '
                elif fig.__class__ == Move:
                    s += str(fig) + ' '
                else:
                    s += fig.__repr__() + ' '
            s += '\n'
        s += '  _________________________'
        s += '\n  |H |G |F |E |D |C |B |A |\n'
        return s

    def get_figure(self, current):
        while True:
            try:
                figure = convertmove(
                    input('Enter coords of cel with figure u want 2 move: [LD]\nL - Letter, D - Digit\n'))
                cfigure = self.field[figure[1]][figure[0]]
                if cfigure.team != current: raise WrongCell
            except WrongCell:
                pass
            except (IndexError, ValueError):
                WrongCell()
            else:
                break
        cfigure.x = figure[1]
        cfigure.y = figure[0]
        return cfigure

    def clear(self):
        for i, line in enumerate(self.field):
            for j, cell in enumerate(line):
                if cell.__class__ == Move:
                    self.field[i][j] = self.field[i][j].figure

    def make_move(self):
        global chosen
        while True:
            try:
                move = convertmove(input('Enter coords of move:\n'))
                if move[1] < 0:
                    self.clear()
                    raise Cancel
                move = move[1], move[0]
                if not move in moves:
                    raise WrongMove

                self.clear()
                self.field[move[0]][move[1]] = chosen
                self.field[chosen.x][chosen.y] = Space()

                if isinstance(chosen, Goose):
                    #промеж. координаты
                    mid_x, mid_y = (chosen.x + move[0]) // 2, (chosen.y + move[1]) // 2
                    mid_cell = self.field[mid_x][mid_y]

                    # Проверяем союзная ли фигура и чётный ли результат броска кубика
                    d6 = random.randint(1, 6)
                    print(f'На кубике выпала цифра: {d6}')
                    if mid_cell.team == chosen.team and d6 % 2 == 0:
                        self.field[mid_x][mid_y] = Space()
                        print("Союзная фигура удалена")

                chosen.x = move[0]
                chosen.y = move[1]
            except WrongMove:
                pass
            except (IndexError, ValueError):
                WrongMove()
            else:
                break
        print(self)

    def find_king(self, king_team):
        for i, x in enumerate(self.field):
            for j, y in enumerate(x):
                if y.__class__ == King and y.team == king_team:
                    return y


class ChessException(Exception): pass


class EndOfTheGame(ChessException):
    def __init__(self):
        print('King is dead\n')


class WrongCell(ChessException):
    def __init__(self):
        print('There\'s no your figure!\n')


class WrongMove(ChessException):
    def __init__(self):
        print('U can\'t move your figure there!\n')


class MouseOnTheEdge(ChessException):
    def __init__(self):
        print('Mouse became another figure!\n')


class Cancel(ChessException): pass


class Check(ChessException):
    def __init__(self):
        print('ШАХ')


class Figure(Battlefield):
    def __init__(self, team):
        self.team = team

    def __repr__(self):
        if isinstance(self, Space):
            return '__'
        elif isinstance(self, King):
            return f"{'w' if self.team == White else 'b'}K"
        elif isinstance(self, Queen):
            return f"{'w' if self.team == White else 'b'}Q"
        elif isinstance(self, Rook):
            return f"{'w' if self.team == White else 'b'}R"
        elif isinstance(self, Knight):
            return f"{'w' if self.team == White else 'b'}N"
        elif isinstance(self, Goose):
            return f"{'w' if self.team == White else 'b'}G"
        elif isinstance(self, Mouse):
            return f"{'w' if self.team == White else 'b'}M"
        else:
            return "?"


    def underAttack(self, battlefield, team, mode='common'):  # team - под атакой какой команды
        x = self.x
        y = self.y
        s = team.side
        show = battlefield.field
        attackers = []

        if mode == 'common':
            return Rook.show_moves(self, battlefield, 'check', team=team) \
                or Knight.show_moves(self, battlefield, mode='check', team=team) \
                or Goose.show_moves(self, battlefield, mode='check', team=team)
        if mode == 'WhoAttack':
            attackers += Rook.show_moves(self, battlefield, 'WhoAttack', team)
            attackers += Mouse.show_moves(self, battlefield, 'WhoAttack', team)
            attackers += Goose.show_moves(self, battlefield, mode='WhoAttack', team=team)
            attackers += Knight.show_moves(self, battlefield, mode='WhoAttack', team=team)
            attackers += King.show_moves(self, battlefield, mode='WhoAttack', team=team)
            return attackers



class Space:

    def __repr__(self):
        return '__'
    def __init__(self):
        self.side = 0
        self.team = Team()


class Mouse(Figure):
    def show_moves(self, battlefield, mode='common', team=0):
        x, y = self.x, self.y
        show = battlefield.field
        moves = []
        s = self.team.side

        if mode == 'WhoAttack':
            attackers = []
            show = battlefield.field[:][:]


        if (self.team == White and x == 0) or (self.team == Black and x == 7):
            raise MouseOnTheEdge


        if y - 1 >= 0:
            #диагональ влево
            if show[x + s][y - 1].__class__ == Space:
                if mode == 'common':
                    show[x + s][y - 1] = Move(show[x + s][y - 1])
                    moves.append((x + s, y - 1))

        if y + 1 < 8:
            #диагональ вправо
            if show[x + s][y + 1].__class__ == Space:
                if mode == 'common':
                    show[x + s][y + 1] = Move(show[x + s][y + 1])
                    moves.append((x + s, y + 1))

        # Атака
        if show[x + s][y].team.side == self.team.enemy:
            if mode == 'common':
                show[x + s][y] = Move(show[x + s][y])
                moves.append((x + s, y))
            if mode == 'WhoAttack' and show[x + s][y].team == team:
                attackers.append(show[x + s][y])

        if mode == 'common':
            print(battlefield)
            return moves
        elif mode == 'WhoAttack':
            return attackers




class Rook(Figure):
    def show_moves(self, battlefield, mode='common', AddMoves=-1, AddShow=-1, team=0):
        x = self.x
        y = self.y
        check = [zip(range(x + 1, 8), generator(y, 7 - x)),
                 zip(range(x - 1, -1, -1), generator(y, x)),
                 zip(generator(x, 7 - y), range(y + 1, 8)),
                 zip(generator(x, y), range(y - 1, -1, -1))]

        if AddMoves == -1:
            moves = []
        else:
            moves = AddMoves

        if AddShow == -1:
            show = battlefield.field
        else:
            show = AddShow

        if mode == 'check':
            show = battlefield.field[:][:]
        if mode == 'WhoAttack':
            attackers = []
            show = battlefield.field[:][:]

        for gen in check:
            for i, j in gen:
                cell = show[i][j]
                if (cell.__class__ == Rook or cell.__class__ == Queen) and cell.team == team:
                    if mode == 'check':
                        return True
                    if mode == 'WhoAttack':
                        attackers.append(cell)
                        break
                if cell.__class__ == Space or cell.team.side == self.team.enemy:
                    if mode == 'common' or mode == 'additional':
                        show[i][j] = Move(cell)
                        moves.append((i, j))
                    if cell.team.side == self.team.enemy:
                        break
                else:
                    break

        if mode == 'common':

            print(battlefield)
            return moves
        elif mode == 'additional':
            return moves, show
        elif mode == 'check':
            return False
        elif mode == 'WhoAttack':
            return attackers


class Knight(Figure):
    def show_moves(self, battlefield, mode='common',
                   team=0):  # team - команда, чьи фигуры надо чекать если mode == 'check'
        check = [(-2, 1), (-2, -1), (2, 1),
                 (2, -1), (1, 2), (-1, 2),
                 (1, -2), (-1, -2)]
        x = self.x
        y = self.y
        moves = []
        if mode == 'common':
            show = battlefield.field
        elif mode == 'check':
            show = battlefield.field[:][:]  # Мб вызываю неправильно (посмотри на аргументы AddMoves и team)
        elif mode == 'WhoAttack':
            show = battlefield.field[:][:]
            attackers = []

        for i, j in check:
            try:
                if x + i < 0 or y + j < 0: raise IndexError

                cell = show[x + i][y + j]
                if cell.__class__ == Knight and cell.team == team:
                    if mode == 'check':
                        return True
                    if mode == 'WhoAttack':
                        attackers.append(cell)
                elif mode == 'common' and (cell.__class__ == Space or cell.team.side == self.team.enemy):
                    show[x + i][y + j] = Move(cell)
                    moves.append((x + i, y + j))
            except IndexError:
                pass

        if mode == 'common':

            print(battlefield)
            return moves
        elif mode == 'check':
            return False
        elif mode == 'WhoAttack':
            return attackers




class Goose(Figure):
    def show_moves(self, battlefield, team=0, mode='common', AddMoves=None, AddShow=None):
        x, y = self.x, self.y
        moves = AddMoves if AddMoves is not None else []
        show = AddShow if AddShow is not None else battlefield.field

        if mode == 'check':
            show = battlefield.field[:][:]  # Deep copy of the board
        elif mode == 'WhoAttack':
            attackers = []
            show = battlefield.field[:][:]

        enemy = Black if self.team == White else White

        # Списки возможных ходов для гуся
        diagonals = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        straight_steps = [(2, 0), (-2, 0), (0, 2), (0, -2)]

        for dx, dy in diagonals:
            try:
                if not (0 <= x + dx < 8 and 0 <= y + dy < 8):
                    continue
                cell = show[x + dx][y + dy]
                if cell.__class__ == Space or cell.team == enemy:
                    if mode == 'common':
                        show[x + dx][y + dy] = Move(cell)
                        moves.append((x + dx, y + dy))
                    elif mode == 'WhoAttack' and cell.team == enemy:
                        attackers.append(cell)
            except IndexError:
                pass

        for dx, dy in straight_steps:
            try:
                dest_x, dest_y = x + dx, y + dy
                if not (0 <= dest_x < 8 and 0 <= dest_y < 8):
                    continue
                dest_cell = show[dest_x][dest_y]

                if dest_cell.__class__ == Space or dest_cell.team == enemy:
                    if mode == 'common':
                        show[dest_x][dest_y] = Move(dest_cell)
                        moves.append((dest_x, dest_y))


                    elif mode == 'WhoAttack' and dest_cell.team == enemy:
                        attackers.append(dest_cell)
            except IndexError:
                pass

        if mode == 'common':
            print(battlefield)
            return moves
        elif mode == 'WhoAttack':
            return attackers
        elif mode == 'check':
            return False



class Queen(Figure):
    def show_moves(self, battlefield):
        AMoves, AShow = Rook.show_moves(self, battlefield, 'additional')
        return Goose.show_moves(self, battlefield, 0, 'common', AMoves, AShow)


class King(Figure):
    def show_moves(self, battlefield, mode='common', team=0):
        x = self.x
        y = self.y
        moves = []
        if mode == 'common':
            show = battlefield.field
        elif mode == 'check':
            show = battlefield.field[:][:]
        elif mode == 'WhoAttack':
            show = battlefield.field[:][:]
            attackers = []
        if self.team == White:
            enemy = Black
        else:
            enemy = White
        try:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0 or x + i < 0 or y + j < 0: continue
                    try:
                        cell = show[x + i][y + j]
                        if not cell.underAttack(battlefield, enemy) and (cell.__class__ == Space or cell.team == enemy):
                            if mode == 'common':
                                show[x + i][y + j] = Move(cell)
                                moves.append((x + i, y + j))
                            if mode == 'WhoAttack':
                                attackers.append(cell)
                                raise ChessException
                    except IndexError:
                        pass
        except ChessException:
            pass

        if mode == 'common':
            print(battlefield)
            return moves
        if mode == 'WhoAttack':
            return attackers


class Move(Figure):
    def __init__(self, figure):
        self.figure = figure
        self.team = figure.team

    def __repr__(self):
        if self.figure.__class__ == Space:
            return 'XX'
        return self.figure.__repr__().lower()


waiting = Black
current = White
battlefield = Battlefield()
print(battlefield)

while True:
    try:
        chosen = battlefield.get_figure(current)
        moves = chosen.show_moves(battlefield)

        battlefield.make_move()
        print(battlefield)

        """Найти короля. Если король под ударом и есть свободные клетки, - шах
           Если король под ударом, свободных нет, но фигура, бьющая короля под ударом - шах
           Если король под ударом, свободных нет, фигура, бьющая короля - одна:
                   можно закрыться - шах
                   нельзя - мат
            бьющих фигур >= 2: мат"""

        king = battlefield.find_king(waiting)
        condition = king.underAttack(battlefield, current)
        if condition:
            raise Check
        print(condition)
    except Check:
        if len(King.show_moves(battlefield, 'WhoAttack')) == 0:
            attackers = King.underAttack(battlefield, current, 'WhoAttack')

            if len(attackers) > 1:
                print(attackers)
                print("Много аткующих")
                break

            attacker = attackers[0]
            if attacker.underAttack(battlefield, waiting, 'WhoAttack'):  # чота не так
                print('Check!')
            else:
                print("Атакующий не под атакой!!")
                break
        else:
            print("Check")


    except MouseOnTheEdge:
        print("Мышь достигла края доски и должна быть превращена.")
        new_piece = input("Выберите новую фигуру для превращения (Q - ферзь, R - ладья, N - конь, G - гусь): ").upper()

        if new_piece == "Q":
            battlefield.field[chosen.x][chosen.y] = Queen(current)
        elif new_piece == "R":
            battlefield.field[chosen.x][chosen.y] = Rook(current)
        elif new_piece == "N":
            battlefield.field[chosen.x][chosen.y] = Knight(current)
        elif new_piece == "G":
            battlefield.field[chosen.x][chosen.y] = Goose(current)
        else:
            battlefield.field[chosen.x][chosen.y] = Queen(current)  # Выбор по умолчанию — ферзь

        print("Мышь превращена в новую фигуру.")
        print(battlefield)

    except EndOfTheGame:
        print("EndOfTheGame Exception")
        break
    except ChessException:
        pass
    finally:
        current, waiting = waiting, current
print('и МАТ!\nКоманда', current.__name__, "выиграла!")





