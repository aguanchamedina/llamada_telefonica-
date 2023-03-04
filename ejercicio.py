# COSTO DE LLAMADA TELEFÓNICA 
print("------------------------------------------")
print("-----------COSTO DE LLAMADA---------------")
print("------------------------------------------")

# INPUT
minutos = int(input("Digite los minutos de llamada: "))

# PROCESS
if minutos <= 3:
    costo = 300
else:
    costo = (minutos-3) * 50 + 300

# OUTPUT
print("La cantidad a pagar es de $" + str(costo))

 