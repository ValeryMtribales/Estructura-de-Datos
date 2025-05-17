class VerificadorBalanceo:
    def __init__(self, expresion: str):
        self.expresion = expresion
        self.pila = []
        self.pares = {')': '(', '}': '{', ']': '['}

    # Método para verificar si la expresión está balanceada
    def verificar_balanceo(self) -> bool:
        for caracter in self.expresion:
            if caracter in '({[':  
                # Si es un símbolo de apertura, se agrega a la pila
                self.pila.append(caracter)
            elif caracter in ')}]':  
                # Si es un símbolo de cierre, verifica si la pila está vacía o si el tope no coincide
                if not self.pila or self.pila.pop() != self.pares[caracter]:
                    return False  
        # Si la pila está vacía al final, la expresión está balanceada
        return not self.pila  

    def __str__(self) -> str:
        return f'La expresión {self.expresion} está balanceada: {self.verificar_balanceo()}'


expresion1 = VerificadorBalanceo('[{()}]')  
print(expresion1)

expresion2 = VerificadorBalanceo(']')
print(expresion2)