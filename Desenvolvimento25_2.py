#Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa.
#Este programa que ler uma seqüência de caracteres, e mostra e diz se é um palíndromo ou não
inicio = str(input("Digite uma seqüência de caracteres \n"))
meio = inicio.replace(" ", "") #remove os espaços
fim = meio[::-1]

if meio == fim:
    print('É palíndromo \n ',inicio ,'<----->', inicio[::-1])

else:
    print('Não é palíndromo \n',inicio ,'<----->', inicio[::-1])