# distance = int(input("Растояние в км:"))
# speed_car = int(input("Планирумая среднаяя скорость в :"))
# time = distance * 60 // speed_car
# print(distance, "километров:"  " ", "Вы проеедете за", time, "минут!")
buy_car = input("what do you need a car:")
name_car = input("Name the car model:")
model_car = input("Wich to buy the brand a car?:")
cost_car = int(input("How much to spend money that to buy a car?:"))
service = int(input("maintenance cost,'Стоимость ТО':"))
fuel = int(input("Cost for fuel:"))
tax = int(input("What the price for tax on the car?:"))
insurance = int(input("what the price for insurance?:"))
total = cost_car + service + fuel + tax + insurance

print("For All:", total)
