class MinhaClasse:
    def __init__(self, atributo1, atributo2=42, atributo3=None):
        self.atributo1 = atributo1
        self.atributo2 = atributo2
        self.atributo3 = atributo3
      
    def metodo_funcional1 (self):
        return f"Isso é um método funcional 1 com atributo1 = {self atributo1}"
    
    def metodo_funcional2(self):
        return f"Isso é um método funcional 2 com atributo2 = {self .atributo2}"

    def __str__(self):
        return f"Atributo1: {self.atributol}, Atributo2: {self.atributo2}, Atributo3: {self.atributo3}"


if __name__ == "__main__":
    objeto1 = MinhaClasse (10, 20, "ABC")
    objeto2 = MinhaClasse (5, 15)
    objeto3 = MinhaClasse (2)
  
    print (objeto1)
    print (objeto2)
    print (objeto3)

    objeto1.atributo1 = -5
    objeto3.atributo3 = None

    print (objeto1.metodo_funcional1())
    print (objeto2.metodo_funcional2())
