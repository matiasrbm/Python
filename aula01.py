def linha():
    print("-" * 50)


def mostrar_dados(self):
    print("- Nome: ", self.nome)
    print("- Idade: ", self.idade)
    print("- Obra: ", self.obra)


class Construtor:
    def __init__(self, nome, idade, obra):
        self.nome = nome
        self.idade = idade
        self.obra = obra

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_idade(self):
        return self.idade

    def set_idade(self, nova_idade):
        self.idade = nova_idade

    def get_obra(self):
        return self.obra

    def set_obra(self, nova_obra):
        self.obra = nova_obra


if __name__ == '__main__':
    construtor1 = Construtor("Pedro", 52, "Torre de Ibiza")
    construtor2 = Construtor("Filipe", 60, "Estátua da Liberdade")
    construtor3 = Construtor("Rodrigo", 44, "Túnel Rei Péle")

    linha()
    print("Nome do Construtor 1:", construtor1.get_nome())
    print("Idade:", construtor1.get_idade())
    print("Principal obra:", construtor1.get_obra())

    linha()
    print("Nome do Construtor 2:", construtor2.get_nome())
    print("Idade:", construtor2.get_idade())
    print("Principal obra:", construtor2.get_obra())

    linha()
    print("Nome do Construtor 3:", construtor3.get_nome())
    print("Idade:", construtor3.get_idade())
    print("Principal obra:", construtor3.get_obra())
    linha()

    construtor1.set_nome("Plinio")
    construtor2.set_nome("Paulo")
    construtor3.set_nome("Julio")

    print("\nApós atualizações --> ")
    print("Nome do Construtor 1:", construtor1.get_nome())
    print("Idade:", construtor1.get_idade())
    print("Principal obra:", construtor1.get_obra())

    linha()
    print("Nome do Construtor 2:", construtor2.get_nome())
    print("Idade:", construtor2.get_idade())
    print("Principal obra:", construtor2.get_obra())

    linha()
    print("Nome do Construtor 3:", construtor3.get_nome())
    print("Idade:", construtor3.get_idade())
    print("Principal obra:", construtor3.get_obra())
    linha()
    linha()

    construtor1.set_nome("Plinio")
    construtor2.set_nome("Paulo")
    construtor3.set_nome("Julio")