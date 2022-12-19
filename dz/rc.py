import csv

class Rc:
    def __init__(self, nm, flrs, hght, wdth):
        self.nm, self.flrs, self.hght, self.wdth = nm, flrs, hght, wdth
        
    def to_tuple(self):
        return self.nm, self.flrs, self.hght, self.wdth
    
    @classmethod
    def from_tuple(cls, data):
        return cls(*data)

    def __str__(self):
        return f'Название: {self.nm}\n Количество этажей: {self.flrs}\n Высота здания: {self.hght}\n Ширина здания: {self.wdth}\n'

def rc():
    print('\nВведите "1/создать/create - Чтобы создать здание"' '\nИли "2/посмотреть/look - Чтобы увидеть уже существующие здания"\n')
    inp = input().lower() #читает любое слово с большой или маленькой буквы
    create, look = ['1', 'создать', 'create',], ['2', 'посмотреть', 'look']
    if inp in create:
        print('Создание здания...\nВведите название здания: ', end='')
        name = input()
        print('Введите кол-во этажей: ', end='')
        floors = input()
        print('Введите высоту здания: ', end='')
        height = input()
        print('Введите ширину здания: ', end='')
        width = input()
        try:        
            if int(floors) > 0 and int(height) > 0 and int(width) > 0:
                building = Rc(name, int(floors), int(height), int(width))
                with open('rc', 'a') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerow([building.nm, building.flrs, building.hght, building.wdth])
                    print('Здание успешно построено!')
            else:
                print(' Ошибка! Высота, ширина и кол-во этажей должны быть больше нуля!')
        except ValueError:
            print('Ошибка! Введенные данные высоты, ширины и кол-ва этажей должны быть числами!')
    elif inp in look:
            with open('rc', 'rt') as file:
                csv_reader = csv.reader(file)
                for line in csv_reader:
                    # читает тип переданных аргументов и форматирует строку
                    print(Rc(line[0],line[1],line[2],line[3]))
                   
            with open('rc', 'rt') as file:
                csv_reader = csv.reader(file)
                rc_csv = [Rc.from_tuple(row) for row in csv_reader]
                print('Количество построенных зданий на данный момент:', len(rc_csv))
            
rc()