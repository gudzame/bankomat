money = int(input("Введите сумму, которую хотите снять: "))
while money > 100000 or money < 1:
    money2 = int(input("Введена некорректная сумма! Попробуйте еще раз: "))
summa = []
if (money // 10000) == 1:
    if (money // 1000) == 10:
        summa.append("десять")
    elif (money // 1000) == 11:
        summa.append("одинадцать")
    elif (money // 1000) == 12:
        summa.append("двенадцать")
    elif (money // 1000) == 13:
        summa.append("тринадцать")
    elif (money // 1000) == 14:
        summa.append("четырнадцать")
    elif (money // 1000) == 15:
        summa.append("пятнадцать")
    elif (money // 1000) == 16:
        summa.append("шестнадцать")
    elif (money // 1000) == 17:
        summa.append("семнадцать")
    elif (money // 1000) == 18:
        summa.append("восемнадцать")
    elif (money // 1000) == 19:
        summa.append("девятнадцать")
elif (money // 10000) == 2:
    summa.append("двадцать")
elif (money // 10000) == 3:
    summa.append("тридцать")
elif (money // 10000) == 4:
    summa.append("сорок")
elif (money // 10000) == 5:
    summa.append("пятьдесят")
elif (money // 10000) == 6:
    summa.append("шестьдесят")
elif (money // 10000) == 7:
    summa.append("семьдесят")
elif (money // 10000) == 8:
    summa.append("восемьдесят")
elif (money // 10000) == 9:
    summa.append("девяносто")
if ((money // 1000) > 9) and ((money // 1000) < 20):
    summa.append("тысяч")
else:
    if (money // 1000) % 10 == 1:
        summa.append("одна тысяча")
    elif (money // 1000) % 10 == 2:
        summa.append("две тысячи")
    elif (money // 1000) % 10 == 3:
        summa.append("три тысячи")
    elif (money // 1000) % 10 == 4:
        summa.append("четыре тысячи")
    elif (money // 1000) % 10 == 5:
        summa.append("пять тысяч")
    elif (money // 1000) % 10 == 6:
        summa.append("шесть тысяч")
    elif (money // 1000) % 10 == 7:
        summa.append("семь тысяч")
    elif (money // 1000) % 10 == 8:
        summa.append("восемь тысяч")
    elif (money // 1000) % 10 == 9:
        summa.append("девять тысяч")

if (money // 100) % 10 == 1:
    summa.append("сто")
elif (money // 100) % 10 == 2:
    summa.append("двести")
elif (money // 100) % 10 == 3:
    summa.append("триста")
elif (money // 100) % 10 == 4:
    summa.append("четыреста")
elif (money // 100) % 10 == 5:
    summa.append("пятьсот")
elif (money // 100) % 10 == 6:
    summa.append("шестьсот")
elif (money // 100) % 10 == 7:
    summa.append("семьсот")
elif (money // 100) % 10 == 8:
    summa.append("восемьсот")
elif (money // 100) % 10 == 9:
    summa.append("девятьсот")

if (money // 10) % 10 == 1:
    if money % 100 == 10:
        summa.append("десять")
    elif money % 100 == 11:
        summa.append("одиннадцать")
    elif money % 100 == 12:
        summa.append("двенадцать")
    elif money % 100 == 13:
        summa.append("тринадцать")
    elif money % 100 == 14:
        summa.append("четырнадцать")
    elif money % 100 == 15:
        summa.append("пятнадцать")
    elif money % 100 == 16:
        summa.append("шестнадцать")
    elif money % 100 == 17:
        summa.append("семнадцать")
    elif money % 100 == 18:
        summa.append("восемнадцать")
    elif money % 100 == 19:
        summa.append("девятнадцать")
elif (money // 10) % 10 == 2:
    summa.append("двадцать")
elif (money // 10) % 10 == 3:
    summa.append("тридцать")
elif (money // 10) % 10 == 4:
    summa.append("сорок")
elif (money // 10) % 10 == 5:
    summa.append("пятьдесят")
elif (money // 10) % 10 == 6:
    summa.append("шестьдесят")
elif (money // 10) % 10 == 7:
    summa.append("семьдесят")
elif (money // 10) % 10 == 8:
    summa.append("восемьдесят")
elif (money // 10) % 10 == 9:
    summa.append("девяносто")
if ((money % 100) < 20) and ((money % 100) > 9):
    summa.append("рублей")
else:
    if money % 10 == 1:
        summa.append("один рубль")
    elif money % 10 == 2:
        summa.append("два рубля")
    elif money % 10 == 3:
        summa.append("три рубля")
    elif money % 10 == 4:
        summa.append("четыре рубля")
    elif money % 10 == 5:
        summa.append("пять рублей")
    elif money % 10 == 6:
        summa.append("шесть рублей")
    elif money % 10 == 7:
        summa.append("семь рублей")
    elif money % 10 == 8:
        summa.append("восемь рублей")
    elif money % 10 == 9:
        summa.append("девять рублей")
    elif money % 10 == 0:
        summa.append("рублей")
summa[0] = summa[0].capitalize()
print(*summa)