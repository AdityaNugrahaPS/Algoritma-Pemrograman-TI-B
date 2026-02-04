cars = ["Ford", "Volvo", "BMW"]

x = cars[0]
cars[0] = "Toyota"
x = len(cars) #arr length
for x in cars:
  print(x) #print all
  cars.append("Honda") #add
  cars.pop(1) #remove