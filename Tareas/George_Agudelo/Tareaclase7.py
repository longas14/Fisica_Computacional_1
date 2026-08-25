def convertir_a_binario(numero):
    if numero == 0:
        return "0"
    
    binario = ""
    n = abs(numero)
    
    while n > 0:
        residuo = n % 2
        binario = str(residuo) + binario  
        n = n // 2  
        
    return binario

num = int(input("Ingresa un número entero: "))
print(f"El número {num} en binario es: {convertir_a_binario(num)}")