#Declare your age as integer variable
edad=19
#Declare your height as a float variable
altura=1.66
#Declare a variable that store a complex number
num_complex=4+6j
#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
print("Area de un triangulo")
base=float(input("Ingresa tu base \n"))
altura=float(input("Ingresa tu altura \n"))
area=((0.5*base)*altura)
print(f"el area de tu triangulo es de {area}")
#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a=float(input("Ingresa el lado a de tu triangulo"))
b=float(input("Ingresa el lado b de tu triangulo"))
c=float(input("Ingresa el lado c de tu triangulo"))
print(f'El perimetro de su triangulo es: {a+b+c}')
#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(not(len('python')==len('dragon')))
#Use and operator to check if 'on' is found in both 'python' and 'dragon'
p, d = "python", "dragon"
print(bool(p.index("on") and d.index("on")))
#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sent="I hope this course is not full of jargon"
print(bool(sent.index("jargon")))
#There is no 'on' in both dragon and python
print(not(bool(p.index("on") and d.index("on"))))
#Find the length of the text python and convert the value to float and convert it to string
a=str(float(len("python")))
print(a)
#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
even_or_not=float(input("ingrese un numero"))
if 0 != even_or_not%2 :
  print("no es par")
else:
  print("es par")
#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7//3==2.7)
#Check if type of '10' is equal to type of 10
print(type("10")==type(10))
#Check if int('9.8') is equal to 10
print(int(9.8)==10)
#Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
ganancia=float(input("Cuanto gana por hora?"))
horas=float(input("Cuantas horas trabaja a la semana"))
salario=(ganancia*horas)*4
print(f"Su salario mensual es de {salario}")
#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
edad=float(input("cuantos anos tienes"))
segundos=edad*12*30*24*60*60
print(f"Usted a vivido aproximadamente {segundos} segundos")
