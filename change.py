def change():
    expense = 23.75
    money = 100
    pesos = int(money - expense) 
    centavos = (money - expense) - pesos
    print(f"""Ingresar gasto:
{expense}
Dinero recibido
{money}

Vuelto

Pesos:
{pesos}
Centavos:
{centavos}
""")
    
change()
