def aniversario():
    sair = 0
    while (sair == 0):
        Nome = input("Digite seu nome completo \n")
        
        Ano = int(input("Digite o ano que você nasceu \n"))
        try:
            if (Ano >= 1922) and (Ano <= 2021) and (Nome.replace(" ", "").isalpha()):# terceira condição remove todos os espaços em branco da string
                idade = 2022 - Ano
                sair = 1
            else:
                sair = 0
                idade = 1/sair  #condição para gerar erro caso os requisitos não sejam atendidos
            Nome = Nome.lower() #deixa todas as letras minusculas
            Nome = Nome.title() # deixa as primeiras letras dos nomes proprios maiuscula
            print(Nome)
            print(idade,'anos')
            
        except:
            print("Erro, tente novamente!")
        
aniversario()