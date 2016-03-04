"""This code indicates the expense of someone on a trip"""
def hotel_cost(nights):
    return nights * 140
    
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
        
def rental_car_cost(day):
    if day >= 7:
        return (day * 40) - 50
    elif day >= 3:
        return (day * 40) - 20
    else:
        return day * 40
        
def trip_cost(city, day, spending_money):
	"""Spending_money it indicates how much more you will take the trip"""
    return rental_car_cost(day) + hotel_cost(day) + plane_ride_cost(city) + spending_money 

"""test"""	
print trip_cost("Los Angeles",5,600)