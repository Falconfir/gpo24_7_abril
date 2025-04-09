class Cuadrado:
    def __init__(self,lado1,lado2):
        self.lado1=lado1
        self.lado2=lado2

    def area (self):
        return self.lado1 * self.lado2

lado1=int(input("ingresa un lado"))
lado2=int(input("ingresa otro lado"))
cuadrado= Cuadrado(lado1, lado2)
resultado= cuadrado.area()

print(f"el resultado es{resultado}")