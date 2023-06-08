def z1():
    a = input("Введите пароль")
    b = input("Введите пароль ещё раз")
    if a == b:
        print("Пароль принят")
    else:
        print("Пароль не принят")

def z2():
    place = int(input("Введите номер вашего места"))
    if place % 2 == 0 and place < 54:
        print ("Верхнее место")
    elif place % 2 != 0 and place < 54:
        print ("Нижнее место")
    elif place >= 37 and place <= 54:
        print ("Боковое место")
    else:
        print("Купе-место")


def z3():
    year = int(input("Введите год"))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print (year, "високосный")
    else:
        print ("Этот год не високосный")


def z4():
    color1 = input("Введите первый цвет")
    color2 = input("Введите второй цвет")
    if (color1 == "красный" and color2 == "синий") or (color1 == "синий" and color2 == "красный"):
        print("фиолетовый цвет")

    elif (color1 == "красный" and color2 == "желтый") or (color1 == "желтый" and color2 == "красный"):
        print("оранжевый цвет")

    elif (color1 == "синий" and color2 == "желтый") or (color1 == "желтый" and color2 == "синий"):
        print("зелёный цвет")

    else:
        print("невозможно смешать цвета")
z1(),z2(),z3(),z4()