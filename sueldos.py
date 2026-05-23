print("\033c")
trabajadores = 0
sueldos = 0
respuesta = 's'
def aumentos(horas, pago_hora):
    sueldo_base = horas * pago_hora
    if horas == 10:
        aumento = sueldo_base * 0.20  
    elif horas == 15:
        aumento = sueldo_base * 0.30  
    elif horas == 20:
        aumento = sueldo_base * 0.15  
    elif horas >= 25:                 
        aumento = sueldo_base * 0.08  
    else:
        aumento = 0                   

    return sueldo_base + aumento
while respuesta == 's':
    print("\n--- Registro ---")
    nombre = input("Ingrese su nombre: ")
    num_horas = int(input("Ingrese el número de horas trabajadas: "))
    sueldo_hora = float(input("Ingrese el sueldo por hora: "))
    
    sueldo_neto = aumentos(num_horas, sueldo_hora)
    
    sueldos += sueldo_neto
    trabajadores += 1
    
    print(f"Sueldo neto de {nombre}: ${sueldo_neto:.2f}")
    
    respuesta = input("\n¿Desea ingresar otro registro? (s/n): ").lower()
print(f"El número total de trabajadores registrados es: {trabajadores}\nEl sueldo neto total de todos los trabajadores es: ${sueldos:.2f}")