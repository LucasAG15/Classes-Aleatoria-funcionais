import random


class PokemonAleatorio:
    def __init__(self, nome):
        self.nome = nome
        self.tipos = self.gerar_tipos()
        self.sexualidade = self.gerar_sexualidade()
        self.status = self.gerar_status()

    def gerar_tipos(self):
        tipos_disponiveis = ["Inseto", "Planta", "Fada", "Normal", "Dragão", "Psíquico",
                             "Fantasma", "Terra", "Ferro", "Fogo", "Voador", "Gelo",
                             "Elétrico", "Pedra", "Dark", "Água", "Lutador", "Venenoso"]

        # Escolhe 1 ou 2 tipos aleatórios
        num_tipos = random.randint(1, 2)
        tipos_escolhidos = random.sample(tipos_disponiveis, num_tipos)
        return tipos_escolhidos

    def gerar_sexualidade(self):
        opcoes = ["Masculino", "Feminino", "Sem gênero"]
        return random.choice(opcoes)

    def gerar_status(self):
        return {
            "HP": random.randint(30, 200),
            "Ataque": random.randint(30, 200),
            "Defesa": random.randint(30, 200),
            "Ataque Especial": random.randint(30, 200),
            "Defesa Especial": random.randint(30, 200),
            "Velocidade": random.randint(30, 200)
        }

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
    print("=== Gerador de Pokémon Aleatório ===")
    nome = input("\nDigite o nome do seu Pokémon: ")

    pokemon = PokemonAleatorio(nome)
    pokemon.mostrar_pokemon()
