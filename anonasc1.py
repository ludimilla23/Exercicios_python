import datetime
ano_nasc = int(input("Digite o ano que você nasceu: "))
ano_atual = datetime.datetime.now().year
idade = ano_atual - ano_nasc
print(f"Você tem {idade} anos.")