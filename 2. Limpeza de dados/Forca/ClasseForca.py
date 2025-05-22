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
        print(" |       ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
                

    if(chances == 1):
        print(" |      😬   ")
        print(" |      👕    ")
        print(" |            ")
        print(" |            ")
        

    if(chances == 2):
        print(" |      😬   ")
        print(" |     -👕  ")
        print(" |            ")
        print(" |            ")
        
        

    if(chances == 3):
        print(" |      😬   ")
        print(" |     -👕-   ")
        print(" |            ")
        print(" |            ")

    if(chances == 4):
        print(" |      😬   ")
        print(" |     -👕-   ")
        print(" |      🩳     ")
        print(" |            ")
              

    if(chances == 5):
        print(" |      😬   ")
        print(" |     -👕-   ")
        print(" |      🩳     ")
        print(" |     /     ")
    

    if (chances == 6):
        print(" |      😵   ")
        print(" |     -👕-   ")
        print(" |      🩳     ")
        print(" |     /   \   ")
        
        
    print(" |            ")
    print("_|___         ")
    print()



class Forca:

    #Método Construtor
    def __init__(self, palavras):
        self.palavra = palavras
        self.letras_erradas = []
        self.letras_escolhidas = []

    #método para advinhar a letra
    def Find_Words(self, letra):

        #Se a letra estiver dentro da palavra e não estiver na lista de letras escolhidas
        if letra in self.palavra and letra not in self.letras_escolhidas:

            #Adiciona a letra na lista de letras escolhidas
            self.letras_escolhidas.append(letra)

        #Senão-se a letra não estiver na palavra e não estiver na lista de letras erradas
        elif letra not in self.palavra and letra not in self.letras_erradas:
            
            #Adiciona a letra na lista de letras erradas
            self.letras_erradas.append(letra) 

        else:            
            return False
                
        return True


    def Forca_Win(self):
        if '_' not in self.Hide_Palavras():
            return True
        return False


    #Método para verificar se o jogo terminou
    def Forca_End(self):
        #retorna True se o jogador ganhou ou se o número de letras erradas for igual a 6
        return self.Forca_Win() or len(self.letras_erradas) == 6

        
    #Método para não mostrtar a letra no Board 
    def Hide_Palavras(self):
        
        rtn = ''

    #Para cada letra na palavra
        for letra in self.palavra:
        #se a letra não estiver na lista de letras escolhidas
            if letra not in self.letras_escolhidas:
                #Adiciona um '_' na string
                rtn += '_'
            else:
                #Adiciona a letra na string
                rtn += letra
        #Retorna a string        
        return rtn
    
    #Método para checar o status do game e imprimir o board
    def Print_Game_Status(self):

        tentativas_restantes = 6 - len(self.letras_erradas)
        
        desenha_forca(len(self.letras_erradas))
        print('\nPalavra: ' + self.Hide_Palavras())
        print(f"Tentativas restantes: {tentativas_restantes}")
        print('\nLetras erradas: ', ' '.join(self.letras_erradas))
        print('Letras corretas: ', ' '.join(self.letras_escolhidas))
        

def Randon_Palavra():
    #Lista de palavras para o jogo
    palavras = ["melancia", "brocolis", "repolho", "maracujá", "jilo", "abacate", "uva", "morango", "laranja", "cabelinho", "cenoura", "beterraba", "berinjela", "abobrinha", "aspargo", "alcachofra", "nabo"]
    #Escolhe uma palavra aleatória da lista acima

    palavra = random.choice(palavras)

    #retorna a palavra
    return palavra
    

def main():
    
    limpa_tela()

    #Escolhe uma palavra aleatória da lista acima
    game = Forca(Randon_Palavra())

    print("Bem-vindo ao jogo da Forca!")
    #enquanto o jogo não terminar
    while not game.Forca_End():
        
        game.Print_Game_Status()

        while True:
            user_input = input('\nDigite uma letra: ').lower().strip()
            print("______________________________________________________________________________________\n")

            # Valida se é uma única letra e se é alfabética
            if len(user_input) != 1 or not user_input.isalpha():
                print("Entrada inválida. Digite apenas uma letra (sem números, espaços ou símbolos).")
                continue

            # Verifica se a letra já foi usada
            if user_input in game.letras_escolhidas or user_input in game.letras_erradas:
                print("Você já tentou essa letra. Tente outra.")
                continue

            break 

        # Aplica a jogada com a letra válida
        game.Find_Words(user_input)

        

    #verifica se o jogador ganhou
    game.Print_Game_Status()
    
    #se o jogador ganhou
    if game.Forca_Win():
        limpa_tela()
        game.Print_Game_Status()
        print('\nParabéns! Você ganhou!\n')

    else:
        #verifica se o jogador ganhou
        limpa_tela()
        game.Print_Game_Status()
        print('\nVocê perdeu! A palavra era: ' + game.palavra + '\n')

#Instrução que indica que é pra iniciar o programa
if __name__ == "__main__":
    main()