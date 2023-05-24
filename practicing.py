from datetime import datetime

fruta = "laranjas"
quantidade = 6
precoLaranja = 8/12

print("preciso comprar %d %s que estao saindo a R$%f/unidade" %(quantidade, fruta, precoLaranja))

print("preciso comprar {} {} que estao saindo a R${:.2f}/unidade ".format(quantidade, fruta, precoLaranja))

print (f"Preciso comprar {quantidade} {fruta} que estão saindo a R${precoLaranja:.2f}/unidade")
print (f"Preciso comprar {quantidade:03} {fruta} que estão saindo a R${precoLaranja:.2f}/unidade")

birthday = datetime(1993, 2, 14)
sentence = f"Daniel has a birthday in {birthday}"
sentence = f"Daniel has a birthday in {birthday:%B %d, %Y}"
print(sentence)