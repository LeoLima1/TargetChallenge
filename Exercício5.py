def inverter_string(s):
    caracteres = list(s)
    caracteres.reverse()
    string_invertida = ''.join(caracteres)

    return string_invertida

string = input("Informe uma string para inverter: ")

resultado = inverter_string(string)
print("string original:", string)
print("string invertida:", resultado)