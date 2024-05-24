from Funciones_matematicas import *
def menu() -> str:
    print(f"{'Menu de opciones':^50}")
    print("1- Ingreso de primero operador")
    print("2- Ingreso del segundo operador")
    print("3- Calcula todas las operaciones")
    print("4- Informar resultados")
    print("5- Salir")
    return input("Ingrese opcion:")

seguir = "s"
while seguir == "s":
    match menu()    :
        case "1":
            try:
                a = int(input("Ingrese el primer operador: "))           
            except:
                print(TypeError("El valor A ingresado no es un entero"))           
        case "2":
            try:
                b = int(input("Ingrese el segundo operador: "))
            except:
                print(TypeError("El valor B ingresado no es un entero"))  
        case "3":              
            print(f"numero a calcular A:{a} y B:{b}")
            resultado_suma =suma(a,b)
            resultado_resta =resta(a,b)
            resultado_division = division(a,b)
            resultado_multiplicacion =multiplicar(a,b)
            resultado_factorial =factorial(a,b)   
        case "4":
            try:
                print(f"“El resultado de A+B es: {resultado_suma}")
                print(f"El resultado de A-B es: {resultado_resta}")
                print(f"la division es: {resultado_division}")
                print(f"El resultado de A*B es: {resultado_multiplicacion}")
                print(f"El factorial de A y B es: {resultado_factorial}")
            except:
                print("No se pudo calcular las operaciones")
        case "5":
            break
            

print("Fin del programa")