import xml.etree.ElementTree as et

def rc():
    print('\nВведите "1/создать/create - Чтобы создать дом"' '\nИли "2/посмотреть/look - Чтобы увидеть уже существующие здания"\n')
    inp = input().lower() #читает любое слово с большой или маленькой буквы
    create, look = ['1','create', 'создать'], ['2', 'look', 'посмотреть']
    tree = et.ElementTree(file='rc.xml') #Мы можем импортировать эти данные, прочитав из файла
    root = tree.getroot() # Возвращает корневой элемент для этого дерева.
    if inp in create:
        print('Создание здания...\nВведите название здания: ', end='') #Позволяет предотвратить разрыв строки
        n = input()
        print('Введите количество этажей: ', end='')
        f = input()
        print('Введите высоту здания: ', end='')
        h = input()
        print('Введите ширину здания: ', end='')
        w = input()
        try:
            if int(f) and int(h) and int(w) > 0: 
                building = root[0]
            else:
                print('Ошибка! Высота, ширина и количество этажей должны быть больше нуля!')
        except ValueError:
            print('Ошибка! Введенные данные высоты, ширины и количества этажей должны быть числами!')   
        name, flrs, hght, wdth = et.Element("NAME_RC"), et.Element("NUMBER_OF_FLOORS_IN_THE_RC"), et.Element("RC_HEIGHT"), et.Element("RC_WIDTH")
        name.text, flrs.text, hght.text, wdth.text = n, f, h, w
        building.append(name), building.append(flrs), building.append(hght), building.append(wdth), tree.write('rc.xml')
        print('Здание успешно построено!')
            
    elif inp in look:
        counter = 0
        for build in root[0]:
            if "RC_WIDTH" in build.tag:
                print(build.tag + ":", build.text, '\n')
                counter += 1
            else:
                print(build.tag + ":", build.text) #полное текстовое содержимое  равно данному text.
        print('Количество зданий = {0}'.format(counter))
    else:
        print('Такой команды не существует')   
rc()