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
