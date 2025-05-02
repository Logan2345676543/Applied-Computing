people = int(input("How many people ate dinner? "))
dinner = float(input("How much did dinner cost? "))
tip = int(input("How mcuh percent do you want to tip? "))
tip_pay = (dinner + tip*100/100)/people
print("Each person has to pay $", tip_pay,)
distance = int(input("How many kms are you going ? "))
cost = distance*0.45
print("The taxi will cost $",cost)
Total = dinner + cost + tip_pay
print("The total night cost $", Total)
Total_each = tip_pay + cost
print("each person will spend $", Total_each)