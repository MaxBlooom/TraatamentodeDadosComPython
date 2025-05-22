import random
from os import system, name

def limpa_tela():
    """Limpa a tela do console."""
    #Windows
    if name == 'nt':
        _ = system('cls')
    #Mac
    else:
        _ = system('clear')


def desenha_forca(chances):
    print("  _______     ")
    print(" |/      |    ")

    if(chances == 0):
        print(" |      😵   ")
        print(" |     -👕 -   ")
        print(" |      🩳     ")
        print(" |     /   \   ")        

    if(chances == 1):
        print(" |      😬   ")
        print(" |     -👕 -   ")
        print(" |      🩳     ")
        print(" |     /     ")
        

    if(chances == 2):
        print(" |      😬   ")
        print(" |     -👕 -   ")
        print(" |      🩳     ")
        print(" |            ")
        

    if(chances == 3):
        print(" |      😬   ")
        print(" |     -👕 -   ")
        print(" |            ")
        print(" |            ")

    if(chances == 4):
        print(" |      😬   ")
        print(" |     -👕  ")
        print(" |            ")
        print(" |            ")
        

    if(chances == 5):
        print(" |      😬   ")
        print(" |      👕    ")
        print(" |            ")
        print(" |            ")

    if (chances == 6):
        print(" |      😬 ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        
    print(" |            ")
    print("_|___         ")
    print()


def game():

    limpa_tela()

    # Lista de palavras para o jogo
    palavras = ["melancia", "abacate", "uva", "morango", "laranja"]

    # Escolhe uma palavra aleatória da lista acima
    palavra = random.choice(palavras)  
    letras_adivinhadas = ['_' for letra in palavra]

    # Numero de Chances
    chances = 7

    # Lista para as Letras Erradas
    letras_erradas = []

    print("Bem-vindo ao jogo da Forca!")
    print("Adivinhe a palavra abaixo.\n")

   
    while chances > 0:

        #Print 
        print ("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))
        desenha_forca(chances)
        print ("Palavra:","".join(letras_adivinhadas))

        # Tentativa
        tentativa = input("\nDigite uma Letra: " ).lower()
        limpa_tela()

        # Verifica se a tentativa é válida
        if not tentativa.isalpha() or len(tentativa) != 1:
            print("Por favor, digite apenas uma letra.")
            continue

        if tentativa in palavra:
            index = 0

            for p in palavra:
                if tentativa == p:
                    letras_adivinhadas[index] = tentativa
                index += 1
        else:
            chances -= 1 
            letras_erradas.append(tentativa)
        
        if "_" not in letras_adivinhadas:
            print("\nParabéns! Você adivinhou a palavra:", palavra)
            break
        
    if "_" in letras_adivinhadas:
        print("\nVocê perdeu! A palavra era:", palavra)
        desenha_forca(chances)

        

# Chama a função para iniciar o jogo
if __name__ == "__main__":
    game()
    print("\nObrigado!")
# End of the code
