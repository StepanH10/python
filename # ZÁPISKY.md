# ZÁPISKY
## Štěpán Hodboď 1IT
### [Github](https://github.com/StepanH10)
# Stringy
- stringy jsou základ pythonu
- dají se sčítat mezi sebou ALE NE S INT
```python
text = "HELLO "
text2 = "WORLD"
```
- Když dáme string do 3x "" bude víceřádkový
- opakovat můžeme *
```python
print ("hello world" * 3)
```
- Řetězce lze spojovat (+), opakovat (*), řezat ([start:end]).
 - Pomocí len() zjistíš délku textu.
 - Používej lower(), upper(), strip(), replace(), split()  pro úpravy textu.
-  f-string je nejlepší způsob pro vkládání proměnných do textu.



# Promněné
- základ pythonu
- ukládá hodnotu do proměné npř. x
```python
x = 10
y = 20
xy = 10 + 20
```
# Print
- Další základ pythonu
- díky print dokážeme rozpovídát počítač
```python
x = 10
y = "Hello world"
print (x)
print (y)
```
---
# Input
- způsob jak vložit něco do proměné
```python
a = input("enetr your age")
print (f"your age is {a}")
```
- jestli chcete sčítat s danou proměnou musíte vložit int
```python
a = int(input("eneter your age"))
ab = a + 10
print (f"your age + 1O is {ab}")
```
# Strip 

- Používá se na vyčištění textu  
```python
Txt = ("AHAhaHAhaHAh") 
Txt = Txt.Strip()
```
# Lower 

- Všechno se dá do malích písmen 
```python
Txt = ("AHAhaHAhaHAh") 
Txt = Txt.lower() 
```
# Split 
- Rozdělí tetxt podle mezer 
```python
Txt = ("AHAhaH  AhaHAh") 
Txt = Txt.split() 
```
# Slovník
- klíče si určuju já
- místo [ ] { }
```python
slovnik = {
    "colors": ["red","green"]
    "number": 3
    "boolean" True
}

print (slovnik ["colors"] ["1"])
```
# Barvy
```python
print("\033[31mThis is red text\033[0m")   # Red text
print("\033[32mThis is green text\033[0m")  # Green text
```
- 30 = Black
- 31 = Red
- 32 = Green
- 33 = Yellow
- 34 = Blue
- 35 = Magenta
- 36 = Cyan
- 37 = White


# If Elif Else
- rovná se: a == b
- nerovná: a != b
- méně než: a < b
- méně než nebo rovno: a <= b
- větší než: a > b
- větší než nebo rovno : a >= b

### If
```python
a = 33
b = 22
if a > b:
    print ("a je větší než b")
```

### Elif
- Klíčové slovo elif je způsob, jakým Python říká „pokud předchozí podmínky nebyly pravdivé, zkuste tuto podmínku
```python
a=3
b=2

if a < b:
    print ("a je větší než b")

elif a > b:
    print ("b je větší než a")
```
### Else
- else zachycuje zbytek
```python
a=3
b=2

if a < b:
    print ("a je větší než b")

elif a > b:
    print ("b je větší než a")

else:
    print ("a je rovno b")
    
```

## For Loops
```python
for prvek in sekvence:
    # kód, který se provede v každé iteraci
```
- prvek  název proměnné, která bude v každé iteraci obsahovat jinou hodnotu ze sekvence
- sekvence  objekt, přes který cyklus prochází (např. seznam)
odsazení určuje blok kódu uvnitř cyklu
### (1, 10, 2)
- min, max, po, kolika
```python
for i in range(1,10,2):
    print(i)
```
- output = 1
3
5
7
9

# While
- Smyčka (while loop) se používá k opakovanému provádění bloku kódu, dokud je splněna podmínka.
## syntaxe
```python
x = 0
while x == 10:
    print ("Hello World")
    x = x + 1
```
### Nekonečný while loop
- While true poběží dokud jej nepřerušíme pomocí break
```python
while True:
    odpověď = input("Chceš skončit? (ano/ne): ")
    if odpověď.lower() == "ano":
        break  # Ukončí smyčku
```
### Continue
 - while smyčka s continue (přeskočení iterace)
python
```python
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # Přeskočí číslo 3
    print(i)
```
### Shrnutí
- while smyčka běží, dokud je podmínka pravdivá.
 - Pozor na nekonečné smyčky (nezapomenout měnit - - - hodnotu proměnné).
 - break ukončuje cyklus.
 - continue přeskočí aktuální iteraci a pokračuje dál.
 - else se vykoná, pokud cyklus neskončil breakem.





---
# Aritmetické operace 
- 	Sčítání	
```python
a = 2
b = 1
print (a + b)
```
-	Odčítání
```python
a = 1
b = 2
print (a + b)
```
- 	Násobení
```python
a = 1
b = 2
print (a * b)
```
- 	Dělení (float)
```python
a = 1
b = 2
print (a / b)
```
- 	Celé dělení	(bez zbytku)
```python
a = 1
b = 2
print (a // b)
```
- Zbytek po dělení
```python
a = 1
b = 2
print (a % b)
```
- Umocňování (na druhou)
```python
a = 1
b = 2
print (a ** b)
```
