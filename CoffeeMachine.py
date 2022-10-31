coffee = {1 : "Russiano", 2 : "Kakavo", 3 : "Neskvik s pivom", 4 : "Kosmostars s vodkoi"}
Prices = {"Russiano" : 10, "Kakavo" : 20, "Neskvik s pivom" : 30, "Kosmostars s vodkoi" : 40}

order_num = 0
tovar = ""

money = 0
a = 0
sdacha = 0
def Tovar_and_price():
    price = 0
    print("Доступные товары: ", coffee)
    try:
        order_num = int(input("Введите номер заказа: "))
    except:
        print("Ты ввел не число, дибил.")
        Tovar_and_price()
    if order_num == 392:
        return order_num
    if order_num == 1 or order_num == 2 or order_num == 3 or order_num == 4:
        for k, v in coffee.items():
            if k == order_num:
                tovar = v
                for k, v in Prices.items():
                    if k == tovar:
                        price = v
    else:    
        print("Неверный номер товара\n")
        return 392
    money = int(input(f"Гони столько денег: {price}"))
    if money == price:
        print("Держите ваш напиток!\n")
    elif money > price:
        sdacha = money - price
        print(f"Ваша сдача: {sdacha}\nДержите ваш кофе!\n")
    else: 
        print("Недостаточно деняг :(\n")
while 1:
    Tovar_and_price()
    if Tovar_and_price() == 392:
        break
