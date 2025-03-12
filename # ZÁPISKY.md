# ZÁPISKY
## Štěpán Hodboď 1IT
### [Github](https://github.com/StepanH10)

## Promněné
- základ pythonu
- ukládá hodnotu do proměné npř. x
```python
x = 10
y = 20
xy = 10 + 20
```
## Print
- Další základ pythonu
- díky print dokážeme rozpovídát počítač
```python
x = 10
y = "Hello world"
print (x)
print (y)
```
## Strip 

- Používá se na vyčištění textu  
```python
Txt = ("AHAhaHAhaHAh") 
Txt = Txt.Strip()
```
## Lower 

- Všechno se dá do malích písmen 
```python
Txt = ("AHAhaHAhaHAh") 
Txt = Txt.lower() 
```
## Split 
- Rozdělí tetxt podle mezer 
```python
Txt = ("AHAhaH  AhaHAh") 
Txt = Txt.split() 
```
## Slovník
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
## Barvy
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


## If Elif Else
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
