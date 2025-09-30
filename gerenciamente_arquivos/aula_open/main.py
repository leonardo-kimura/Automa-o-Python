#  arquivo = open("arquivo.txt") #abrir arquivo
# conteudo = arquivo.read()

# print(conteudo)

# arquivo.close() #fechar arquivo

# with open("arquivo.txt") as arquivo:
#     print(arquivo.readlines()) le linhas

# with open("arquivo.txt", 'a', encoding='utf-8') as arquivo:  w-escrever e vai substituir tudo, a-só adicionar
#     arquivo.write("Olá mundo!\n")

with open("arquivo.txt", 'r+', encoding='utf-8') as arquivo: # w+ usa para se caso o arquivo nao exista, porém vai substituir tudo
    arquivo.write("Olá mundo!") #depois que escreve o ponteiro ta no final
    # arquivo.seek(0) #resetar o ponteiro
    arquivo.write("Texto que vem depois")
    print(arquivo.read())