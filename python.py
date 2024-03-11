from random import randint, random

x, y = 1, 2

print(x, y)

x = "5"
y = "5"
print(x, y)

h = int(y)
c = float(x)

print("Hexadecimal: ", hex(h))
print(x)
x = 7.2
y = 3.5
print(x, y)

print(x / y)
print(x % y)
print(x // y)

cadena = "Hola Mundo"

print([c for c in cadena])

print(randint(1, 10), random())

for c in range(10):
    x += randint(1, 10)
    print(x)

x = 0
while x < 1000:
    x += randint(1, 10)
    print(x)


x = 24
y = "A"
if x > 0 and x < 24:
    y = y + "B"
elif x >= 24 and x < 45:
    y = y + "C"
elif x >= 45 and x < 60:
    y = y + "D"
else:
    y = "Z"

print(y)

x = 24
y = "A"
if x > 0 and x <= 24:
    y = y + "B"
if x >= 24 and x < 45:
    y = y + "C"
if x >= 45 and x < 60:
    y = y + "D"
else:
    y += "Z"

print(y)


temperatura = randint(0, 40)
if temperatura <= 18:
    print("Clima Tropical")
if temperatura >= 18:
    print("Que calor!")
if temperatura == 18:
    print("Templado")
else:
    print("Frio o Calor")

print(temperatura)
d = [0, 1, 2, 3, 4, 5, 6]
e = d
e[-1] = 50
d[2] = 40
print(d)
print(e)

l = [10, 30, 50, 70]
l += l[-1:-3]
print(l)

cadena = "anita lava la tina"
tmp = []
for c in cadena:
    tmp.append(c)
tmp.reverse()
nuevaCadena = "".join(tmp)
print(nuevaCadena)
