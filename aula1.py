import math
from collections import Counter
 
# exercicio 1
nome = "sim"
idade = 12
altura = 1.3
cidade = "gotham"
print(f"{nome}, {idade} anos, {altura}m, mora em {cidade}")

#exercicio 2
frutas = ["banana", "melão", "pera", "maça", "melancia"]
print(frutas)
frutas.append("goiaba")
frutas.append("kiwi")
print(frutas)
frutas.remove("kiwi")
print(frutas)

#exercício 3
notas = [6, 4, 7, 10, 9, 8.5, 8.8]
media = 0
for i in range(len(notas)):
    media += notas[i]
media = media/len(notas)
print(media)
print(min(notas))
print(max(notas))

#exercício 4
lista = [x for x in range(1,21, 2)]
print(lista)

#exercício 5
pessoa = {
    "nome": "2343252432543",
    "nome2": "39856301895",
    "nome3": "73652307097"
}
print(pessoa["nome2"])

#exercicio 6
def recebaTuplas(tupla1, tupla2):
    distancia = math.sqrt((tupla2[0] - tupla1[0])**2 + (tupla2[1] - tupla1[1])**2)
    return distancia

print(recebaTuplas((2, 3), (6, 5)))

#exercício 7
frase = "o luiz veste mano do gueto, luiz"
palavras = frase.split()
contador = Counter(palavras)
print(contador)

#exercicio 8
def estatisticas(*numeros):
    media = 0
    for i in range(len(numeros)):
        media += numeros[i]
    media = media/len(numeros)
    return {"media": media, "max": max(numeros), "min":min(numeros)}


numeros = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(estatisticas(*numeros))

#exercício 9
class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def repor(self, quantidade):
        if(quantidade <= 0):
            print("valor invalido")
        else:
            self.estoque += quantidade

    def vender(self, quantidade):
        if(quantidade <= 0):
            print("pode nao")
        elif(self.estoque >= quantidade):
            self.estoque -= quantidade
        else:
            print("estoque insuficiente")

    def exibir(self):
        print(f"o produto{self.nome} tem {self.estoque} unidade disponiveis com preço unitário de {self.preco}")


#exercicio 10
class Veiculos:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def tipoHabilitacao(self):
        return "sla"


class Carro(Veiculos):
    def tipoHabilitacao(self):
        return "categoria B (Carro)"
    
class Moto(Veiculos):
    def tipoHabilitacao(self):
        return "categoria A (moto)"
    
veiculo = Carro("toyota", "corolla")
veiculo2 = Moto("honda", "cg160c")

print(f"{veiculo.modelo}:{veiculo.tipoHabilitacao()}")
