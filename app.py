class Veiculo:
    def __init__(self, modelo, ano, valor):
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def get_modelo(self):
        return self.modelo
        
    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo

    def get_ano(self):
        return self.ano
        
    def set_ano(self, novo_ano):
        self.ano = novo_ano

    def get_valor(self):
        return self.valor
        
    def set_valor(self, novo_valor):
        self.valor = novo_valor

    def mostrar_dados(self):
        print("Modelo:", self.modelo)
        print("Ano:", self.ano)
        print("Valor:", self.valor)
        
    def retorno_dados(self):
        dados = f"Modelo: {self.get_modelo()}, Ano: {self.get_ano()}, Valor: {self.get_valor()}"
        return dados
    
    def aumenta_valor(self, aumento):
        if aumento >= 0:
            self.valor += aumento
        else:
            print("Erro: Aumento deve ser um valor positivo.")

if __name__ == "__main__":
    veiculo1 = Veiculo("Up", 2018, 62999.00)
    veiculo2 = Veiculo("Renault Kwid", 2020, 58990.00)
    veiculo3 = Veiculo("Hyundai HB20", 2022, 69990.00)
    veiculo4 = Veiculo("Fiat Cronos", 2023, 84790.00)

    print("veiculo1:")
    print("Modelo:", veiculo1.get_modelo())
    print("Ano:", veiculo1.get_ano())
    print("Valor:", veiculo1.get_valor())
    aumento = float(input("\nDigite o valor do aumento: "))
    veiculo1.aumenta_valor(aumento)

    
    print("veiculo2:")
    print("Modelo:", veiculo2.get_modelo())
    print("Ano:", veiculo2.get_ano())
    print("Valor:", veiculo2.get_valor())
    aumento = float(input("\nDigite o valor do aumento: "))
    veiculo2.aumenta_valor(aumento)
    
    print("veiculo3:")
    print("Modelo:", veiculo3.get_modelo())
    print("Ano:", veiculo3.get_ano())
    print("Valor:", veiculo3.get_valor())
    aumento = float(input("\nDigite o valor do aumento: "))
    veiculo3.aumenta_valor(aumento)
    
    print("veiculo4:")
    print("Modelo:", veiculo4.get_modelo())
    print("Ano:", veiculo4.get_ano())
    print("Valor:", veiculo4.get_valor())
    aumento = float(input("\nDigite o valor do aumento: "))
    veiculo4.aumenta_valor(aumento)