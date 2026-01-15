
#1. Declare a function add_two_numbers. It takes 
# two parameters and it returns a sum.
def sum(num1, num2):
  res = num1 + num2
  return res
print(sum(1, 2))
#2. Area of a circle is calculated as follows: 
# area = π x r x r. Write a function that calculates
#  area_of_circle.
def area_of_circle(r):
  r = float(r)
  area = 3.1416*r*r
  return area
print(area_of_circle(3))
#3. Write a function called add_all_nums which takes
#  arbitrary number of arguments and sums all the 
# arguments. Check if all the list items are number
#  types. If not do give a reasonable feedback.
def add_all_nums(*nums):
  sum=0
  for i in nums:
    sum += i
  return sum
print(add_all_nums(10,9))
#4. Temperature in °C can be converted to °F using 
# this formula: °F = (°C x 9/5) + 32. Write a function
#  which converts °C to °F, convert_celsius_to-fahrenheit.
def temp_convert_C_to_F (temp):
  temp = float(temp)
  F = (temp*9/5) + 32
  return F
print(temp_convert_C_to_F(1))
#5. Write a function called check-season, it takes a
#  month parameter and returns the season: Autumn, Winter,
#  Spring or Summer.
def check_season(mes):
  spring = ["march", "april", "may"]
  summer = ["june", "july", "august"]
  autumn = ["september", "october", "november"]
  winter = ["december", "january", "february"]
  season = [spring, summer, autumn, winter]
  season_names = ["spring", "summer", "autumn", "winter"]
  for i in range(len(season)): 
    for j in season[i]:
      if mes != j:
        pass
      else:
        print(season_names[i])
check_season("december")