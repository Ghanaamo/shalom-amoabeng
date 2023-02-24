#civil engineering 
#6926921







# A list of cars available and their prices

cars={
"Rolls Rocyce Phantom":1700000,
"Benz C Class":3400000,
"Toyota Corrolla":2450000,
"Toyota Tundra":7800000,
"Mercedes Maybach":5678000,
"Range Rover Sport":9000000,
"Lexus":9800000,
"Ferrari 458 Italia":8000000,
"Ferrari 488 GTB":7540000,
"Ferrari F430":6600000,
"Ferrari F40":8960000,
"Porsche 911":6340000,
"Porsche  Panamera":7890000,
"porsche Macan":7940000,
"Honda Civic":8888000,
"Honda CR-V":77778900,
"Honda Domani":9999000,
"Mercedes-Benz W164 M-Class":6464000,
"Mercedes-Benz W245 B-Class":4356000,
"BMW 3 Series":7899000,
"BMW 5 Series":8799000,
"BMW X3":5068070,
"BMW X1":8690433,
"Audi A3":9756000,
"Audi A5 Sportback":8777623,
"Tesla model 3":8654321,
"Tesla model y":4444564,
"Nissan Rogue":5567000,
"Nissan Sentra":7654000,
"Twingo":7897000,
}
# get user input for car name
Car_name = input("Enter a car_name:")
# check if car name is in the list of available cars
if Car_name in cars:
    print("Yes")
    #if car name is present,get its price
    Car_price=cars[Car_name]
    print(f"The price of {Car_name} is ${Car_price}")
else:
    #if car name is not present, inform the user
    print(f"Sorry, {Car_name} is not available.")