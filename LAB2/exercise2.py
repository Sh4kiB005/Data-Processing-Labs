"""
 Create a tuple containing six temperature readings: three
for Saturday and three for Sunday. Use a for loop to display each reading and calculate the highest and
lowest temperatures. Label the readings in your output where appropriate.

"""

temperatures = (28, 30, 32, 27, 29, 31)

days = ("Saturday", "Saturday", "Saturday",
        "Sunday", "Sunday", "Sunday")

highest = temperatures[0]
lowest = temperatures[0]

for i in range(len(temperatures)):
    print(days[i], "temperature:", temperatures[i])

    if temperatures[i] > highest:
        highest = temperatures[i]

    if temperatures[i] < lowest:
        lowest = temperatures[i]

print("Highest temperature:", highest)
print("Lowest temperature:", lowest)