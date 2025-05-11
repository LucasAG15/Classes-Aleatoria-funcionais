class CriarPokemon:
    def __init__(self):
        print("\n--- Crie seu Pokémon ---")
        self.nome = input("Digite o nome do seu Pokémon: ")
        self.tipos = self.definir_tipos()
        self.sexualidade = self.definir_sexualidade()
        self.status = self.definir_status()

    def definir_tipos(self):
        tipos_disponiveis = ["inseto", "planta", "fada", "normal", "dragão", "psiquico", "fantasma", "terra",
                             "ferro", "fogo", "voador", "gelo", "elétrico", "pedra", "dark", "água", "lutador", "venenoso"]

        tipos_disponiveis_lower = [tipo.lower() for tipo in tipos_disponiveis]

        print("\nTipos disponíveis:", ", ".join(tipos_disponiveis))
        tipos = []

        while len(tipos) < 2:  # Permite até 2 tipos
            tipo = input(f"Digite o {len(tipos)+1}º tipo: ").lower().strip()

            if tipo in tipos_disponiveis_lower:
                # Encontra a versão correta com capitalização original
                index = tipos_disponiveis_lower.index(tipo)
                tipo_corrigido = tipos_disponiveis[index]

                if tipo_corrigido not in tipos:
                    tipos.append(tipo_corrigido)
                    print(f"Tipo {tipo_corrigido} adicionado!")
                else:
                    print("Este tipo já foi adicionado!")
            else:
                print("Tipo inválido! Escolha entre:",
                      ", ".join(tipos_disponiveis))

            if len(tipos) >= 1:
                adicionar_mais = input(
                    "Deseja adicionar outro tipo? (s/n): ").lower()
                if adicionar_mais != 's':
                    break

        return tipos

    def definir_sexualidade(self):
        print("\nSexualidade disponíveis:")
        print("1 - Masculino")
        print("2 - Feminino")
        print("3 - Sem gênero")
        opcao = input("Escolha a sexualidade (1-3): ")
        if opcao == '1':
            return "Masculino"
        elif opcao == '2':
            return "Feminino"
        else:
            return "Sem gênero"

    def definir_status(self):
        print("\nDefina os atributos do Pokémon (valores de 1 a 200):")
        return {
            "HP": self.obter_valor("HP"),
            "Ataque": self.obter_valor("Ataque"),
            "Defesa": self.obter_valor("Defesa"),
            "Ataque Especial": self.obter_valor("Ataque Especial"),
            "Defesa Especial": self.obter_valor("Defesa Especial"),
            "Velocidade": self.obter_valor("Velocidade")
        }

    def obter_valor(self, atributo):
        while True:
            try:
                valor = int(input(f"{atributo}: "))
                if 1 <= valor <= 200:
                    return valor
                print("Valor deve ser entre 1 e 200!")
            except ValueError:
                print("Digite um número válido!")

    def mostrar_pokemon(self):
        print("\n--- Seu Pokémon ---")
        print(f"Nome: {self.nome}")
        print(f"Tipos: {', '.join(self.tipos)}")
        print(f"Sexualidade: {self.sexualidade}")
        print("Status:")
        for atributo, valor in self.status.items():
            print(f"  {atributo}: {valor}")


# Programa principal
if __name__ == "__main__":
    print("Bem-vindo ao Criador de Pokémon!")
    while True:
        meu_pokemon = CriarPokemon()
        meu_pokemon.mostrar_pokemon()

        continuar = input("\nDeseja criar outro Pokémon? (s/n): ").lower()
        if continuar != 's':
            print("Até logo, Treinador!")
            break
