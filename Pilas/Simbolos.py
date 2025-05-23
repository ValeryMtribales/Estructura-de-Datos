def verificar_balanceo(expresion):
    pila = PilaNodos()
    # No usamos diccionario, solo ifs para cada caso
    for simbolo in expresion:
        if simbolo == '(' or simbolo == '{' or simbolo == '[':
            pila.push(simbolo)
        elif simbolo == ')':
            tope = pila.pop()
            if tope != '(':
                return False
        elif simbolo == '}':
            tope = pila.pop()
            if tope != '{':
                return False
        elif simbolo == ']':
            tope = pila.pop()
            if tope != '[':
                return False
    if pila.vacia():
        return True
    else:
        return False


expresiones = ["{[()()]}", "[(])", "{(a+b) * [c/d]}", "[{()}]", "{(a+b]}"]
for expr in expresiones:
    if verificar_balanceo(expr):
        print(expr + ": Balanceado")
    else:
        print(expr + ": No balanceado")