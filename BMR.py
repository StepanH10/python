m_vaha = 13.397
m_vyska = 4.799
m_vek = 5.677

z_vaha = 9.247
z_vyska = 3.098
z_vek = 4.33

pohlavy = input("Zadejte pohlaví m/ž: ")

if pohlavy == "m":

    vaha = int(input("Zadejte váhu: "))
    vyska = int(input("Zadejte výšku: "))
    vek = int(input("Zadejte věk: "))
    ve = m_vek * vek
    vy = m_vyska * vyska
    va = m_vaha * vaha
    BMR = 88.362 + va + vy - ve
    BMR = round(BMR, 2)
    print(f"Vaše BMR je ≈ {BMR} kcal za den")

elif pohlavy == "ž":
    vaha = int(input("Zadejte váhu: "))
    vyska = int(input("Zadejte výšku: "))
    vek = int(input("Zadejte věk: "))
    ve = z_vek * vek
    vy = z_vyska * vyska
    va = z_vaha * vaha
    BMR = 447.593 + va + vy - ve
    BMR = round(BMR, 2)
    print(f"Vaše BMR je ≈ {BMR} kcal za den")