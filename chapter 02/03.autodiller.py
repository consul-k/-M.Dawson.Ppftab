print("\t\t\tАвтодиллер")
value = int(input("Введите стоимость автомобиля без наценок: "))
tax = value / 100 * 5
tax = int(tax)
print("Налог:", tax)
registration_fee = value / 100 * 3
print("Регистрационный сбор:", registration_fee)
agency_fee = int(2500)
print("Агентский сбор:", agency_fee)
price_of_delivery = int(2000)
print("Цена доставки машины к месту назначения:", price_of_delivery)
final_price = value + tax + agency_fee + registration_fee + price_of_delivery
print("\nОкончательная цена:", final_price)
input("\nНажмите Enter, чтобы выйти.")
