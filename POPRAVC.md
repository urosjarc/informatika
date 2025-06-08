## Spirala

Ustvari funkcijo z imenom `spirala`,
Funkcija naj ob klicu nariše neskonèno spiralo

<img src="https://github.com/urosjarc/informatika/blob/main/media/turtle_spirala.png">

<details>

<summary>Prikazi pomoc</summary>

```python
# Funkcija
def funkcija():
  print("Hy")

# Neskoncna zanka
while(True):
  print("Hy")

import turtle
turtle.speed(1) # Nastavi hitrost zelve od 1 do 10.
turtle.forward(100) # Pojdi naprej za 100 pixlov.
turtle.left(90) # Obrni se levo za 90 stopinj.
```

</details>

# Babuska

Ustvari funkcijo z imenom `babuska`,
ki sprejme celoštevilski argument `stevilo`.
Funkcija naj ob klicu nariše toliko babusk, kot je
vrednost argumenta `stevilo`.

<img src="https://github.com/urosjarc/informatika/blob/main/media/turtle_babuske.png">

<details>

  <summary>Prikazi pomoc</summary>

```python
# Funkcija
def funkcija():
  print("Hy")

# Iteracijska zanka
for i in range(0, 9, 1):
  print("Hy")

import turtle
turtle.speed(1) # Nastavi hitrost zelve od 1 do 10.
turtle.circle(100) # Narisi krog z radijem 100 pixlov.
turtle.exitonclick() # Ko uporabnik klikne na zaslon koncaj program.
```

</details>

# Reka

Ustvari funkcijo `reka` ki nariše reko naslednje oblike...

<img src="https://github.com/urosjarc/informatika/blob/main/media/turtle_reka.png">

<details>

<summary>Prikazi pomoc</summary>

```python
import turtle

turtle.forward(100)
turtle.penup()
turtle.pendown()
turtle.left(20)
turtle.right(20)
turtle.speed(-1)
turtle.exitonclick()

def funkcija(a, b):
	return a + b

for i in range(0, 10, 1):
	print(i)

while(True):
	break

if(2 > 3):
	print("Hello")
```

</details>

## Predstavi dvojiško število 1101101 v desetiškem in šestnajstiškem zapisu.

## Koliko bitov potrebujemo èe želimo zapisati katero koli število med -20 in +20 z binarnim sistemom.

## Koliko bo natanènost digitalnega termometra èe temperaturno skalo od -20 stopinj do 100 stopinj predstavi z 1 byte-om?

## Povej vse o tranzistorju

## Digitalno vezje

Sestavi logièno digitalno vezje z vhodnimi stikali S1, S2 ter LED diodami...
ki prikazujejo trenutno kombinacijo stikal...
LED-ice morajo svetiti po naslednji pravilnostni tabeli...

| S1 | S2 | Rdeèa | Oranžna | Zelena |
|----|----|-------|---------|--------|
| 0  | 0  | 0     | 0       | 1      |
| 0  | 1  | 0     | 1       | 1      |
| 1  | 0  | 0     | 0       | 0      |
| 1  | 1  | 1     | 1       | 1      |


## Varnostna vrata

Sestavi digitalno vezje, ki je sestavljeno iz 4 stikal (S1, S2, S3, S4) ter dveh LED-ic (Rdeèa, Zelena).
Èe uporabnik vnese pravilno zaporedje enic in nièel v 4 stikala se bodo vrata odklenila (zelena LED-ica se bo prižgala).
V nasprotnem primeru naj sveti rdeèa LED-ica.
Pravilnostna tabela za željeno vezje je...

| S1  | S2  | S3  | S4  | Rdeèa | Zelena |
|-----|-----|-----|-----|-------|--------|
| 1   | 1   | 0   | 1   | 0     | 1      |
| ... | ... | ... | ... | 1     | 0      |

# 2. LED Semafor (težja naloga)
Sestavi digitalno vezje, ki je sestavljeno iz treh LED-ic (Rdeèa, Oranžna, Zelena) ter dveh stikal (S1, S2).
Pravilnostna tabela za željeno vezje je...

| S1 | S2 | Zelena | Oranžna | Rdeèa |
|----|----|--------|---------|-------|
| 0  | 0  | 0      | 0       | 0     |
| 0  | 1  | 1      | 0       | 0     |
| 1  | 0  | 0      | 1       | 0     |
| 1  | 1  | 0      | 0       | 1     |
