
name = input("Ваше имя: ")
rost = float(input("Ваш рост: "))
ves = float(input("Ваш вес: "))
age = int(input("Ваш возраст: "))
description = ""


print("Привет ", name, ", твой рост ", rost, " и возраст ", age)


if age<10 or age>120 ves <=10 or ves >300 or rost <=0.5 or rost > 3 :
    description = "Введены некорректные данные"
    print(description)
else:
    ind = round(ves/rost**2, 2)
    if ind < 18.5:
        description = "недостаточной массой тела"
    elif ind < 25:
        description = "нормальной массой тела"
    elif ind < 30:
        description = "избыточной массой тела"
    else:
        description = "ожирением"
    print("вы относитесь к людям с ", description, "индекс ", ind )