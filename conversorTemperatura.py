"""
Conversor de temperatura.
Converte temperaturas de Celsius para Farenheit e Kelvin;
Converte temperaturas de Farenheit para Celsius e Kelvin;
Converte temperaturas de Kelvin para Celsius e Farenheit;
"""

def cel_to_farenheit(x):
    temp = x * (9.0/5.0) + 32.0
    return temp

def far_to_celsius(x):
    temp = 5.0 * (x - 32.0) / 9.0
    return temp

def kel_to_celsius(x):
    temp = x - 273.15
    return temp

def cel_to_kelvin(x):
    temp = x + 273.15
    return temp

def far_to_kelvin(x):
    temp = (x - 32) * 5 / 9 + 273.15
    return temp

print("Lista de conversões possíveis\n")

conversao = ['1 - Celsius -> Farenheit', '2 - Farenheit -> Celsius', '3 - Celsius -> Kelvin',
             '4 - Farenheit -> Kelvin', '5 - Kelvin -> Celsius']

for x in conversao:
    print(x)

sel_conversao = int(input("\nSelecione qual conversão deseja realizar: "))

print(f"OPÇÃO SELECIONADA: {sel_conversao}")

temp = float(input("Qual a temperatura a ser convertida: "))

if sel_conversao == 1:
    farenheit = cel_to_farenheit(temp)
    print(f"\n{temp}ºC convertido para Farenheit é igual {farenheit}ºF")

elif sel_conversao == 2:
    celsius = far_to_celsius(temp)
    print(f"\n{temp}ºF convertido para Celsius é igual {celsius}ºC")

elif sel_conversao == 3:
    kelvin = cel_to_kelvin(temp)
    print(f"\n{temp}ºC convertido para Kelvin é igual {kelvin}K")

elif sel_conversao == 4:
    kelvin = far_to_kelvin(temp)
    print(f"\n{temp}ºF convertido para Kelvin é igual {kelvin}K")

else:
    celsius = kel_to_celsius(temp)
    print(f"\n{temp}K convertido para Celsius é igual {celsius}ºC")
