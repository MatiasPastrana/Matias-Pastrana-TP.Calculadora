def suma(a:int,b:int) -> str:
    """Pide numeros por consola y los muestra
    Return:
        int: resultado suma
    """
    return a + b
    
def resta(a:int,b:int) -> int:
    """Pide numeros por consola y los muestra
    Return:
        int: resultado resta
    """
    return a - b

def multiplicar(a:int, b:int) -> int:
    """duplica el valor ingresado
    Args:
        a(int): entero a duplicar
        b(int): entero por el que se multiplica
    Returns:
        int: doble valor del ingresado
    """
    return a * b   

def division(a:int,b:int) -> int:
    """divide el valor ingresado
    Args:
        a(int): dividendo
        b(int): divisor
    
    Returns:
        int: division del valor ingresado
    """
    if b != 0:
        return a / b
    raise ValueError("no se puede divir por cero")

def factorial(a:int,b:int):
    """sacamos factorial de A y B
    Args:
        a(int): entero a factoriar
        b(int): entero a factoriar
    
    Returns:
        int: resultado del factorial de A y B
    """
    if isinstance(a,int)and isinstance(b,int):
        if a < 0 and b < 0:
            raise ValueError("No esta definido el factorial de un negativo")
        fact_a = 1
        fact_b = 1
        for i in range(1,a + 1):
            fact_a *= i
        for i in range(1,b + 1):
            fact_b *= i
        return f"A:{fact_a}---B:{fact_b}"
    else:
        raise TypeError("No es un numero")
    
