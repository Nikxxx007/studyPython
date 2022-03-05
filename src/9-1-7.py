class Rectangle:
    def __init__(self, h, w, x=0, y=0):
        """
        Объявление прямоугольника в координатах
        (x, y) и с высотой, шириной (h, w)
        :param h: Высота,
        :param w: Ширина,
        :param x: Координата по оси X,
        :param y: Координата по оси Y
        """
        if type(x) != int != type(x) != float:
            raise TypeError('Неверный тип для x', type(x))
        if type(y) != int != type(y) != float:
            raise TypeError('Неверный тип для y', type(y))
        if type(h) != int != type(h) != float:
            raise TypeError('Неверный тип для h', type(h))
        if type(w) != int != type(w) != float:
            raise TypeError('Неверный тип для w', type(w))
        if h < 0:
            raise TypeError('Высота не может быть < 0')
        if w < 0:
            raise TypeError('Ширина не может быть < 0')
        self.__rectangle = {
            'x': x,
            'y': y,
            'h': h,
            'w': w
        }

    def get_rectangle(self):
        """
        :return: Возвращает текущие параметры прямоугольника
        """
        return self.__rectangle

    def get_coords(self):
        """
        Возвращает текущие координаты вершин прямоугольника
        [(Левый нижний), (Левый верхний), (Правый верхний), (Правый нижний)] углы
        :return: Array
        """
        x = self.__rectangle['x']
        y = self.__rectangle['y']
        width = self.__rectangle['w']
        height = self.__rectangle['h']
        return [(round(x, 2), round(y, 2)), (round(x, 2), round(y + height, 2)),
                (round(x + width, 2), round(y + height, 2)), (round(x + width, 2), round(y, 2))]

    def set_coords(self, x, y):
        """
        Устанавливает прямоугольнику координаты левого нижнего угла
        :type x: int
        :type y: int
        :param x: Int
        :param y: Int
        :return: Массив с новыми координатами вершин
        """
        if type(x) != int != type(x) != float:
            raise TypeError('Неверный тип для x', type(x))
        if type(y) != int != type(y) != float:
            raise TypeError('Неверный тип для y', type(y))

        self.__rectangle['x'] = round(x, 2)
        self.__rectangle['y'] = round(y, 2)

        return self.get_coords()

    def move_to(self, x, y):
        """
        Смещает прямоугольник относительно текущих координат
        :param x: смещение по оси X
        :param y: смещение по оси Y
        :return: Массив с новыми координатами вершин
        """
        if type(x) != int != type(x) != float:
            raise TypeError('Неверный тип для x', type(x))
        if type(y) != int != type(y) != float:
            raise TypeError('Неверный тип для y', type(y))

        self.__rectangle['x'] += round(x, 2)
        self.__rectangle['y'] += round(y, 2)

        return self.get_coords()

    def resize(self, w, h):
        """
        Меняет размер прямоугольника
        :param w: Желаемая ширина прямоугольника
        :param h: Желаемая высота прямоугольника
        :return: Массив с новыми координатами вершин
        """
        if type(h) != int != type(h) != float:
            raise TypeError('Неверный тип для h', type(h))
        if type(w) != int != type(w) != float:
            raise TypeError('Неверный тип для w', type(w))
        if h < 0:
            raise TypeError('Высота не может быть < 0')
        if w < 0:
            raise TypeError('Ширина не может быть < 0')
        self.__rectangle['w'] = round(w, 2)
        self.__rectangle['h'] = round(h, 2)

    def resize_to(self, w, h):
        """
        Изменение размера прямоугольника относительно текущего размера
        :param w: изменение ширины
        :param h: изменение высоты
        :return: Массив с новыми координатами вершин
        """
        if type(h) != int != type(h) != float:
            raise TypeError('Неверный тип для h', type(h))
        if type(w) != int != type(w) != float:
            raise TypeError('Неверный тип для w', type(w))
        if self.__rectangle['h'] + round(h, 2) < 0:
            raise TypeError('Высота не может быть < 0')
        if self.__rectangle['w'] + round(w, 2) < 0:
            raise TypeError('Ширина не может быть < 0')
        self.__rectangle['w'] += round(w, 2)
        self.__rectangle['h'] += round(h, 2)

        return self.get_coords()

    def combination(self, second_rectangle):
        """
        Строит наименьший прямоугольник, содержащий оба заданных (относительно координат)
        :type second_rectangle: Rectangle
        :param second_rectangle: второй прямоугольник
        :return: Возвращает третий прямоугольник, содержащий оба входных
        """
        if type(second_rectangle) != type(self):
            raise TypeError('Неверный тип для second_rectangle', type(second_rectangle))


        fc = self.get_coords()
        sc = second_rectangle.get_coords()
        min_x = min([i[0] for i in fc] + [i[0] for i in sc])
        max_x = max([i[0] for i in fc] + [i[0] for i in sc])
        min_y = min([i[1] for i in fc] + [i[1] for i in sc])
        max_y = max([i[1] for i in fc] + [i[1] for i in sc])

        return Rectangle(x=min_x, y=min_y, w=max_x-min_x, h=max_y-min_y)

    def intersection(self, second_rectangle):
        """
        Строит зону пересечения исходных прямоугольников
        :type second_rectangle: Rectangle
        :param second_rectangle: второй прямоугольник
        :return: Возвращает новый прямоугольник, являющийся пересечением 2х исходных
        """
        if type(second_rectangle) != type(self):
            raise TypeError('Неверный тип для second_rectangle', type(second_rectangle))

        second_rectangle = second_rectangle.get_rectangle()
        min_h = min(self.__rectangle['h'], second_rectangle['h'])
        min_w = min(self.__rectangle['w'], second_rectangle['w'])

        return Rectangle(h=min_h, w=min_w)

    def intersection_on_flat(self, second_rectangle):
        """
        Строит зону пересечения исходных прямоугольников (на координатной плоскости)
        :type second_rectangle: Rectangle
        :param second_rectangle: второй прямоугольник
        :return: Возвращает новый прямоугольник, являющийся пересечением 2х исходных
        """
        if type(second_rectangle) != type(self):
            raise TypeError('Неверный тип для second_rectangle', type(second_rectangle))

        fr = self.get_coords()
        sr = second_rectangle.get_coords()

        # R1.y < R2.y1 (левый верхний первого ниже правого нижнего второго)
        # R1.y1 > R2.y (правый нижний выше первого правого верхнего второго)
        # R1.x1 < R2.x (правый нижний первого правее левого верхнего второго)
        # R1.x > R2.x1 (левый верхний первого левее правого нижнего второго)
        # Проверка на пересечение прямоугольников на плоскости (от противного)
        cross = not (fr[1][1] < sr[3][1] or fr[3][1] > sr[1][1] or
                     fr[3][0] < sr[1][0] or fr[1][0] > sr[3][0])

        if cross:
            right_x = sr[3][0] if fr[3][0] > sr[3][0] else fr[3][0]
            left_x = fr[1][0] if fr[1][0] > sr[1][0] else sr[1][0]
            upper_y = sr[1][1] if fr[1][1] > sr[1][1] else fr[1][1]
            bottom_y = sr[3][1] if fr[3][1] < sr[3][1] else fr[3][1]
            return Rectangle(x=left_x, y=bottom_y,
                             h=upper_y-bottom_y,
                             w=right_x-left_x)
        else:
            return False






def debug_for_current(i):
    print(
        '''
Дебаг меню:
Редактируемый прямоугольник: {0} 
1) Перемещение прямоугольника
2) Изменение размера прямоугольника
3) Назад
        '''.format(i))
    return input('Введите № пункта меню: ')


def move_rectangle_menu(data):
    print('Перемещение прямоугольника:')
    print('Старые координаты: x: {}; y: {}'.format(data['x'], data['y']))
    print('Введите новые координаты левого нижнего угла:')
    try:
        x = round(float(input('\tВведите координату x: ')), 2)
        y = round(float(input('\tВведите координату y: ')), 2)
        return x, y
    except Exception as e:
        raise Exception('Ошибка перемещения прямоугольника')


def resize_rectangle_menu(data):
    print('Изменение размеров прямоугольника:')
    print('Старые размеры: высота: {}; ширина: {}'.format(data['h'], data['w']))
    print('Введите новые координаты левого нижнего угла:')
    try:
        w = round(float(input('\tВведите ширину прямоугольника:')), 2)
        h = round(float(input('\tВведите высота прямоугольника:')), 2)
        return h, w
    except Exception as e:
        raise Exception('Ошибка перемещения прямоугольника')


def find_combination_menu(rectangles_list):
    print(rectangles_list)
    print('Введите номера прямоугольников для сравнения:')
    try:
        first = int(input('Номер первого прямоугольника: '))
        second = int(input('Номер второго прямоугольника: '))
        return first, second
    except Exception as e:
        raise Exception('Ошибка выбора прямоугольников')

def find_intersection_menu(rectangles_list):
    print(rectangles_list)
    print('Введите номера прямоугольников для поиска пересечения:')
    try:
        first = int(input('Номер первого прямоугольника: '))
        second = int(input('Номер второго прямоугольника: '))
        return first, second
    except Exception as e:
        raise Exception('Ошибка выбора прямоугольников')


def main_menu():
    print(
        '''
Главное меню: 
1) Добавить новый прямоугольник
2) Посмотреть список прямоугольников
3) Редактировать прямоугольник
4) Поиск наименьшего общего прямоугольника
5) Поиск пересечения (относительно прямоугольников)

0) Выход
        '''
    )
    return input('Введите № пункта меню: ')


def new_rectangle_menu():
    print('Добавление нового прямоугольника:')
    print('Введите координаты левого нижнего угла:')
    try:
        x = round(float(input('\tВведите координату x: ')), 2)
        y = round(float(input('\tВведите координату y: ')), 2)
        w = round(float(input('\tВведите ширину прямоугольника:')), 2)
        h = round(float(input('\tВведите высота прямоугольника:')), 2)
        return x, y, w, h
    except Exception as e:
        raise Exception('Ошибка добавления нового прямоугольника')


class Main:
    def __init__(self):
        self.rectangles = [Rectangle(4, 4, 0, 0), Rectangle(4, 4, 1, -1)]  # Предустановленные прямоугольники

    def add_new_rectangle(self, x, y, w, h):
        obj = Rectangle(h, w, x, y)
        self.rectangles.append(obj)

    def move_rectangle(self, x, y, index):
        obj = self.rectangles[index]
        obj.set_coords(x, y)

    def resize_rectangle(self, h, w, index):
        obj = self.rectangles[index]
        obj.resize(w, h)

    def list_of_rectangles(self, ):
        arr = []
        index = 0
        for rect in self.rectangles:
            str = 'Прямоугольник №{} с параметрами: \n\tШирина: {}, \tВысота: {}, ' \
                  '\n\tКоординаты левого нижнего угла: \n\tx: {}; y: {}'.format(index,
                                                                                rect.get_rectangle()['w'],
                                                                                rect.get_rectangle()['h'],
                                                                                rect.get_rectangle()['x'],
                                                                                rect.get_rectangle()['y'])
            arr.append(str)
            index += 1
        return '\n_______________\n'.join(arr)


if '__main__' == __name__:
    menu = Main()
    while True:
        choice = main_menu()
        if '0' in choice:
            print('Завершение')
            exit(1)
        elif '1' in choice:  # добавление нового
            try:
                x, y, w, h = new_rectangle_menu()
                menu.add_new_rectangle(x, y, w, h)
                print(menu.list_of_rectangles())
                input('enter to continue')
            except Exception as e:
                print(e)
        elif '2' in choice:  # список
            print(menu.list_of_rectangles())
            input('enter to continue')
        elif '3' in choice:  # меню изменения
            i = int(input('Введите номер прямоугольника:'))
            while True:
                try:
                    data = menu.rectangles[i].get_rectangle()
                except:
                    print('Ошибка выбора')
                    break
                try:
                    debug_choice = debug_for_current(i)
                    if '3' in debug_choice:  # возврат в главное меню
                        break
                    elif '1' in debug_choice:  # изменение начала координат
                        x, y = move_rectangle_menu(data)
                        menu.move_rectangle(x, y, i)
                    elif '2' in debug_choice:  # изменение размера
                        h, w = resize_rectangle_menu(data)
                        menu.resize_rectangle(h, w, i)

                except Exception as e:
                    print(e)
        elif '4' in choice:
            try:
                r1, r2 = find_combination_menu(menu.list_of_rectangles())
                try:
                    r1 = menu.rectangles[r1]
                    r2 = menu.rectangles[r2]
                    r3 = r1.combination(r2)
                    cords = r3.get_coords()
                    print('Получился прямоугольник с параметрами: \n\tШирина: {}, \tВысота: {}, ' \
                          '\n\tКоординаты левого нижнего угла: \n\tx: {}; y: {}'.format(r3.get_rectangle()['w'],
                                                                                        r3.get_rectangle()['h'],
                                                                                        r3.get_rectangle()['x'],
                                                                                        r3.get_rectangle()['y']))
                    print(
                        '''
Координаты вершин
{}\t\t{}
\t-------
\t|  \t  |
\t-------
{}\t\t{}
                        '''.format(cords[1], cords[2], cords[0], cords[3]))
                except Exception as e:
                    print('Неверный выбор прямоугольников')
            except Exception as e:
                print(e)
        elif '5' in choice:
            try:
                r1, r2 = find_intersection_menu(menu.list_of_rectangles())
                try:
                    r1 = menu.rectangles[r1]
                    r2 = menu.rectangles[r2]
                    r3 = r1.intersection(r2)
                    cords = r3.get_coords()
                    print('Получился прямоугольник с параметрами: \n\tШирина: {}, \tВысота: {}, ' \
                          '\n\tКоординаты левого нижнего угла: \n\tx: {}; y: {}'.format(r3.get_rectangle()['w'],
                                                                                        r3.get_rectangle()['h'],
                                                                                        r3.get_rectangle()['x'],
                                                                                        r3.get_rectangle()['y']))
                    print(
                        '''
Координаты вершин
{}\t\t{}
\t-------
\t|  \t  |
\t-------
{}\t\t{}
                        '''.format(cords[1], cords[2], cords[0], cords[3]))
                except Exception as e:
                    print('Неверный выбор прямоугольников')
            except Exception as e:
                print(e)

