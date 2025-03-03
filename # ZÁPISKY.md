# ZÁPISKY
## Štěpán Hodboď 1IT



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
