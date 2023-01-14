money = input("Введите сумму депозита ")
#money = 100000

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit=[ int(value*int(money)/100) for value in per_cent.values()]

# for value in per_cent.values():  #пробегаем наш словарь извлекаем значения
#     b= value*int(money)/100 # рассчитываем колличество денег за год
#     deposit.append(int(b)) # добавляем рассчитанное выше значение в список deposit
# print("deposit=",deposit) # выводим заполненный список 

print("deposit=",deposit) # выводим заполненный список 

# max=deposit[0]
# for i in deposit:
#     if i>max:
#         max=i
# print("Максимальная сумма, которую вы можете заработать", max)
    
deposit_max = max(deposit) # ищем максимальное значение в списке
print("Максимальная сумма, которую вы можете заработать", deposit_max)# выводим максимальное значение 