class Construtor:
    def __init__(self, nome, sexo, idade):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_sexo(self):
        return self.sexo

    def set_sexo(self, novo_sexo):
        self.sexo = novo_sexo

    def get_idade(self):
        return self.idade

    def set_idade(self, nova_idade):
        self.idade = nova_idade

    def mostra_dados(self):
        print('- Nome:', self.nome)
        print('Sexo:', self.sexo)
        print('Idade:', self.idade)

    def mostra_dados2(self):
        print('- Nome:', self.get_nome())
        print('Sexo:', self.get_sexo())
        print('Idade:', self.get_idade())

    def mostra_dados3(self):
        print('- Nome:', self.get_nome())
        print('Sexo:', self.get_sexo())
        print('Idade:', self.get_idade())

    def retorna_dados(self):
        dados = f'{self.get_nome()}, {self.get_sexo()}, {self.get_idade()}'
        return dados


if __name__ == "__main__":
    construtor1 = Construtor("Paulo", "M", 59)
    construtor2 = Construtor("Jose", "M", 45)
    construtor3 = Construtor("Fernando", "M", 56)
    print("- construtor1:")
    print("Nome:", construtor1.get_nome())
    print("Sexo:", construtor1.get_sexo())
    print("Idade:", construtor1.get_idade())
    print("- construtor2:")
    print(f"Nome: {construtor2.get_nome()}")
    print(f"Sexo: {construtor2.get_sexo()}")
    print(f'Idade: {construtor2.get_idade()}')
    print("- construtor3:")
    print(f"Nome: {construtor3.get_nome()}")
    print(f"Sexo: {construtor3.get_sexo()}")
    print(f'Idade: {construtor3.get_idade()}')
