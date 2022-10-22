from datetime import datetime,timedelta
def capitan(lst,s):
    with open ("cap.txt", 'w')as file: #открываем файл 
        for i in range(len(lst)): #запускаем цикл по длине списка 
            file.writelines("{0}:{1}\n".format((datetime.strptime(s, "%d.%m.%Y")+timedelta(i)),lst[i])) 
            # Записываем в файл cap.txt дату и запись из списка в формате дата: запись 
            # datetime.strptime - модуль, который превращает строку в объект с типом date 
            #\n перенос строки в format передаю аргументы (подставляет текущие значения) 
            #timdelta модуль, который превращает объект с типом int в объект типа date 
capitan(['ХОЧУ КУШАТЬ','ОЧЕНЬ СИЛЬНО','ОПТУСТИТЕ НА ОБЕД'],'22.10.2022')