from datetime import datetime
 
agora = datetime.now()

# if(agora.hour <= 12):
#     print("Bom dia!")
# elif(agora.hour > 12 and agora.hour <= 18):
#     print("Boa tarde!")
# else:
#     print("Boa noite!")

# falta = 12 - agora.month
# print(agora.strftime(f"Hoje é o %mº do ano. Ainda faltam {falta} meses para terminar o ano"))

nome = input("Digite o seu nome: ")
print(agora.strftime(f"Assinatura gerada por {nome} em %d de novembro de %Y às %H:%m"))