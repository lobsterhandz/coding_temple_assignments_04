temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
second_week_temps = temperatures[7:14]
print("Second week temperatures:", second_week_temps)

above_100 = [temp for temp in temperatures if temp > 100]
print("Temperatures above 100:", above_100)

reversed_temps = temperatures[::-1]
selected_days = reversed_temps[4:10]
print("Selected days from reversed list:", selected_days)