ticket_quantity = int(input('Введите колличество ')) #ввод колличества билетов
print("Колличесвто биллетов", ticket_quantity) #отображение колличества билетов 
partial_cost=990 #переменная для записи стоимости билета со скидкой
total_cost=1390 #переменная для записи стоимости билета без скидки
count=0 # счетчик который будет аккумулировать цену в зависимости колличества биллетов 

for _ in range(0,ticket_quantity): # цикл который перебирает билеты 
    visitor_age = int(input('Введите возраст посетителя '))# ввод возраста для обладателя билета
    if 18 <= visitor_age < 25 : # сравнение возраста и определение цены билета
        print("Цена билета", partial_cost)
        count +=partial_cost
    elif  visitor_age >= 25 : # сравнение возраста и определение цены билета
        print("Полная стоимость билета",total_cost)
        count +=total_cost
    else:
        print("Проход бесплатный")

if ticket_quantity >= 3: # сравнение колличества билетов для расчета скидки или без скидки
    final_cost= (count)-(count)*10/100 # формула для расчетов цены билетов со скидкой
    print("Цена билетов c учетом скидки", int(final_cost)) # вывод цены билетов с учетом скидки
else:
    final_cost = (count)# формула для расчетов цены билетов без скидки
    print("Цена билетов без скидки", final_cost) # вывод цены билетов без скидки