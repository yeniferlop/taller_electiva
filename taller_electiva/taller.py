#1.
name = "Luis"
age = 27
favoriteFood = "Pasta con salsa boloñesa"
print(f"Hola!Mi nombre es {name}, tengo {age} años, y mi comida favorita es  {favoriteFood}")

#2.
fullname = input('Ingresa su nombre completo:')
print(f'Hola,{fullname}! Tu nombre tiene {len(fullname.replace(" ", ""))}, excluyendo los espacios')

#3.
increaseSalesPercent = 12.93720081
revenueGrowthPercent = 18.33206078

print(f'Las ventas de la empresa láctea aumentaron un {increaseSalesPercent:.2f}% y '
      f'los ingresos crecieron un {revenueGrowthPercent:.2f}%')

#4.
secretMessage = "aS!Ir waQm  VL!eDafrcnXi n=gS .P,yytahgoln.!"
result= secretMessage[3::2]
print(result)

#5.
text = '''El nombre "Python" viene dado por la
afición de Van Rossum al grupo Monty Python.'''

print(f'Número de palabras en la frase: {len(text.split())}')

#6.
word = "Camila"
print(word.replace('a','e'))

#7.
sentence = '''La historia del lenguaje de
programación Python'''
print(' '.join(sentence.split()[::-1]))