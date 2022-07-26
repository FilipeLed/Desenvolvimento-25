#O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. 
# O jogador poderá errar 6 vezes antes de ser enforcado.
import random
import os
os.system('cls||clear')

erro = 0; m =0

def Ler_arquivo():
    with open("palavras.txt","r") as arquivo:
        texto = arquivo.read()
  
    palavras = texto.replace(",", "").split()

    x = random.randint(1,len(palavras))
    palavra = palavras[x]
    return palavra




palavra = Ler_arquivo()

traco = [" _"]*len(palavra)

while erro < 6:
    Letra = input("\nDigite uma letra: ").upper()

    n = 0
    for i in range(len(palavra)):

        if palavra[i] == Letra:

            traco[i] = Letra
            n = n + 1
            m = m + 1
        

    if n == 0:
        print(f'Você errou pela {erro+1}° vez. Tente de novo!')
        erro = erro + 1
    else:
        forca =''
        for i in range(len(palavra)):
            forca = forca + traco[i]
        print('A palavra é :'+forca+'\n')
    
    if m == len(palavra):
        erro = 6

print('A palavra é :'+palavra+'\n')




