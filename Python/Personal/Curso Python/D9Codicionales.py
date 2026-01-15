#1. Get user input using input(“Enter your age: ”). If user 
#is 18 or older, give feedback: You are old enough to 
#drive. If below 18 give feedback to wait for the missing 
#amount of years. Output:
#edad = int(input("Enter your age \n"))
edad = 15
if edad >= 18:
  print("You are old enough to drive")
else:
  print("Wait for ", 18-edad, " more years")

#2. Compare the values of my_age and your_age using if … else.
#Who is older (me or you)? Use input(“Enter your age: ”) to
#get the age as input. You can use a nested condition to print
#'year' for 1 year difference in age, 'years' for bigger 
#differences, and a custom text if my_age = your_age. Output:
your_age = 16
my_age = 18
dif = (abs(your_age-my_age))
if your_age > my_age:
  print("Im older for ", dif, " years")
elif your_age==my_age:
  print("We are the same age")
else:
  print("You are older than me for ", dif, " years")

#3. Get two numbers from the user using input prompt. If a is 
# greater than b return a is greater than b, if a is less b 
# return a is smaller than b, else a is equal to b. Output:
#basicamente lo mismo que abajo

