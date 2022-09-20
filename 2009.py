def check(year: int, month: int, day: int):
    if month in [1, 3, 5, 7, 8, 10, 12] and 0 < day <= 31:# 1,3,5,7,8,10,12 - 31 день в месяце 
        return True
    elif month in [4, 6, 9, 11] and 0 < day <= 30: # 4,6,9,11 - 30 дней в месяце 
        return True
    elif month == 2:
        if abs(year) % 100 == 0 and abs(year) % 400 == 0 or # abs - функция, которая возращает абсолютные значения чисел. + проценты считают в.года
                abs(year) % 4 == 0 and abs(year) % 100 != 0:
            if 0 < day <= 29:
                return True 
        elif 0 < day <= 28:
            return True
    return False 


print(check(2000,2,29))
