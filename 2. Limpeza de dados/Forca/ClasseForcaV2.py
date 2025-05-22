import random
from os import system, name

def limpa_tela():
    """Limpa a tela do console."""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def desenha_forca(chances):
    print("  _______     ")
    print(" |/      |    ")

    if(chances == 0):
        print(" |      😵   ")
        print(" |     -👕 -   ")
        print(" |      🩳     ")
        print(" |     /   \\   ")        

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

class Forca:

    def __init__(self, palavra):
        self.palavra = palavra  # Corrigido aqui
        self.letras_erradas = []
        self.letras_escolhidas = []

    def Find_Words(self, letra):
        if letra in self.palavra and letra not in self.letras_escolhidas:
            self.letras_escolhidas.append(letra)
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra) 
        else:            
            return False
        return True

    def Forca_Win(self):
        if '_' not in self.Hide_Palavras():
            return True
        return False

    def Forca_End(self):
        return self.Forca_Win() or len(self.letras_erradas) == 7

    def Hide_Palavras(self):
        rtn = ''
        for letra in self.palavra:
            if letra not in self.letras_escolhidas:
                rtn += '_'
            else:
                rtn += letra
        return rtn
    
    def Print_Game_Status(self):
        desenha_forca(len(self.letras_erradas))  # Corrigido aqui
        print('\nPalavra: ' + self.Hide_Palavras())
        print('Letras erradas: ',)
        for letra in self.letras_erradas:
            print(letra,)
        print()
        print('Letras corretas: ',)
        for letra in self.letras_escolhidas:
            print(letra,)
        print()

def Randon_Palavra():
    palavras = [
        "melancia", "brocolis", "repolho", "maracujá", "jiló", "abacate", "uva", "morango", "laranja",
        "cabelinho", "batata-doce", "cenoura", "beterraba", "berinjela", "abobrinha", "pimentão",
        "aspargo", "alcachofra", "nabo"
    ]
    return random.choice(palavras)

def main():
    limpa_tela()
    game = Forca(Randon_Palavra())
    while not game.Forca_End():
        game.Print_Game_Status()
        user_input = input('Digite uma letra: ')
        game.Find_Words(user_input)  # Corrigido aqui

    game.Print_Game_Status()
    if game.Forca_Win():
        print('Parabéns! Você ganhou!')
    else:
        print('Você perdeu! A palavra era: ' + game.palavra)

if __name__ == "__main__":
    main()
