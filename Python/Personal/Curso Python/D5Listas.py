
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages.sort()
print(f"el maximo de edad en la lista es: {max(ages)}")
print(f"el minimo de edad en la lista es: {min(ages)}")

# Find the median age (one middle item or two middle items divided by two)
print(ages)
if len(ages)%2==0:
  medio_atras=ages[int((len(ages)/2)-1)]
  medio_adelante=ages[int((len(ages)/2)+1)]
  mediana = (medio_atras+medio_adelante)/2
  print(mediana)
else:
  mediana = ages[int((len(ages)/2))]
  print(mediana)

# Find the average age (sum of all items divided by their number )
media = (sum(ages))/(len(ages))
print(media)
# Find the range of the ages (max minus min)
rango = max(ages)-min(ages)
print(rango)
# Compare the value of (min - average) and (max - average), use abs() method
comp_minimo = abs(min(ages) - media)
comp_maximo = abs(max(ages) - media)
print(f"{comp_minimo} {comp_maximo}")
# Find the middle country(ies) in the countries list
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
paises=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'] 
primer_mita = paises[0:4]
segunda_mita = paises[4:]
print(primer_mita)
print(segunda_mita)

print(paises)
ch,Ru,Us, Scand = paises.pop(0), paises.pop(0), paises.pop(0), paises
print(ch)
print(Ru)
print(Us)
print(Scand)
