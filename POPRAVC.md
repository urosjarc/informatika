### 1 Spirala

Ustvari funkcijo z imenom `spirala`,
Funkcija naj ob klicu nari�e neskon�no spiralo

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

### 2. Babuska

Ustvari funkcijo z imenom `babuska`,
ki sprejme celo�tevilski argument `stevilo`.
Funkcija naj ob klicu nari�e toliko babusk, kot je
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

### 3. Reka

Ustvari funkcijo `reka` ki nari�e reko naslednje oblike...

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

### 4. Napi�i postopek pretvorbe dvoji�kega �tevila 1101101 v deseti�ki in �estnajsti�ki zapis. Preveril bom ali dejansko razume�, kaj govori� :)

### 5. Napi�i postopek izra�una Koliko bitov potrebujemo, �e �elimo zapisati katero koli �tevilo med -20 in +20 z binarnim sistemom. Preveril bom ali dejansko razume�, kaj govori� :)

### 6. Napi�i postopek Koliko bo natan�nost digitalnega termometra, �e temperaturno skalo od -20 stopinj do 100 stopinj predstavi z 1 byte-om? Preveril bom ali dejansko razume�, kaj govori� :)

### 7. Povej vse o tranzistorju, ampak res vse, pa ne se piflat, ker bom preveril ali dejansko razume�, kaj govori� :)

### 8. Digitalno vezje

Sestavi logi�no digitalno vezje z vhodnimi stikali S1, S2 ter LED diodami...
ki prikazujejo trenutno kombinacijo stikal...
LED-ice morajo svetiti po naslednji pravilnostni tabeli...

| S1 | S2 | Zelena |
|----|----|--------|
| 0  | 0  | 0      |
| 0  | 1  | 1      |
| 1  | 0  | 0      |
| 1  | 1  | 1      |

<details>

<summary>Prikazi pomoc</summary>

<img src="https://github.com/urosjarc/informatika/blob/main/media/cipi.png">

</details>

### 9. Varnostna vrata

Sestavi digitalno vezje, ki je sestavljeno iz 4 stikal (S1, S2, S3, S4) ter dveh LED-ic (Rde�a, Zelena).
�e uporabnik vnese pravilno zaporedje enic in ni�el v 4 stikala se bodo vrata odklenila (zelena LED-ica se bo pri�gala).
V nasprotnem primeru naj sveti rde�a LED-ica.
Pravilnostna tabela za �eljeno vezje je...

| S1  | S2  | S3  | S4  | Zelena |
|-----|-----|-----|-----|--------|
| 1   | 1   | 0   | 1   | 1      |
| ... | ... | ... | ... | 0      |

<details>

<summary>Prikazi pomoc</summary>

<img src="https://github.com/urosjarc/informatika/blob/main/media/cipi.png">

</details>

### 10. LED Semafor

Sestavi digitalno vezje, ki je sestavljeno iz treh LED-ic (Rde�a, Oran�na, Zelena) ter dveh stikal (S1, S2).
Pravilnostna tabela za �eljeno vezje je...

| S1 | S2 | Zelena | Oran�na |
|----|----|--------|---------|
| 0  | 0  | 0      | 0       |
| 0  | 1  | 1      | 0       |
| 1  | 0  | 0      | 1       |
| 1  | 1  | 0      | 0       |

<details>
<summary>Prikazi pomoc</summary>

<img src="https://github.com/urosjarc/informatika/blob/main/media/cipi.png">

</details>

### 11. Iz podane tabele ustvari graf (stolp�ni, �rtni, raztreseni, tortni) in ga siliraj

### 12. Iz podane tabele ustvari vrtilno tabelo in prika�i statistiko iskanega vpra�anja (sortiranje, procenti, povpre�je, vsota, filtriranje)

### 13. Iz podane tabele ustvari vrtilni grafikon in prika�i statistiko iskanega vpra�anja (sortiranje, procenti, povpre�je, vsota, filtriranje)
