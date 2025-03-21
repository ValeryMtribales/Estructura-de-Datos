def verificar_balanceo(expresion):
    pila = []
    pares = {')': '(', '}': '{', ']': '['}

    for simbolo in expresion:
        if simbolo in '({[':
            pila.append(simbolo)  # Agregar a la pila
        elif simbolo in ')}]':
            if not pila or pila.pop() != pares[simbolo]:
                return False  # No está balanceado

    return not pila  # Debe estar vacía para ser balanceado

# Ejemplos de prueba
expresiones = ["{[()()]}", "[(])", "{(a+b) * [c/d]}", "[{()}]", "{(a+b]}"]
for expr in expresiones:
    print(f"{expr}: {'Equilibrado' if verificar_balanceo(expr) else 'No equlibrado'}")