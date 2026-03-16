import numpy as np

# 1
array = np.random.randint(100, 501, size=12)
print(array)

# 2
matriz = array.reshape(3, 4)
print(matriz)

#3
matrizT = matriz.T
soma = sum(matrizT[:])
print(soma)

#4
media = np.mean(matriz, axis=0)
print(media)

# 5
print(len(array[array > 400]))

# 1
print(np.arange(10))

#2
print(np.full([3, 3], True, dtype=bool))

#3
print(array[array % 2 != 0])

#4
array[array % 2 != 0] = -1
print(array)

#5
matriz2 = np.random.randint(1, 101, size = (5, 5))
print(matriz2)

#6
matriz2T = matriz2.T
soma2 = sum(matriz2T[:])
print(soma2)

#7
maximo = np.max(matriz2, axis = 1)
print(maximo)

#8
a = np.array([1, 2, 3, 4, 5])
print(a+2)

#9
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.concat([a, b]))

#10
print(np.flip(a))

#1
temp = np.array([22, 24, 21, 23, 25, 20, 22])
print(np.mean(temp))

#2
vendas = np.random.randint(50, 201, size=12).reshape(3, 4)
print(vendas)
matrizT = vendas.T
soma = sum(matrizT[:])
print(soma)

#3
pont = np.array([75, 88, 92, 65, 70, 80, 95, 60, 85, 78])
print(pont.min())
print(pont.max())

#4
sim = np.random.rand(20)
print(sim)
print(sim[sim > 0.7])

#5
preco = np.array([120.50, 121.00, 119.80, 122.30, 120.00])
percnt = (preco[1:] - preco[:-1])/preco[:-1] * 100
print(percnt)

#6
print(np.eye(4, 4))

#7
print(np.zeros((3, 3)))
print(np.ones((2, 5)))

#8
print(np.random.randint(100, 501, size=25).reshape(5, 5))

#9
sim = np.arange(10)
print(sim[sim % 2 ==0])

#10
array = np.arange(1, 6)
print(np.sum(array))

#11
arr = np.array([1, 2, 2, 3, 4, 4, 4, 5])
print(np.unique(arr))

#12
print(np.linspace(0, 10, 5))

#13
notas = [80, 90, 70]
pesos = [0.3, 0.5, 0.2]
print(np.average(notas, weights=pesos))

#14
dados = np.array([[1.5, 2.0, 3.5],
                  [7.0, 8.5, 9.0]])
print(dados.T)

#15
matriz = np.arange(12).reshape(3, 4)
print(np.flip(matriz, axis=0))

#16
a = np.array([1, 2, 3])
b = np.array([3, 2, 1])
print(a == b)

#17
array = np.random.randint(0, 101, size=10)
print(array[array > 50])

#18
num = [1, 7, 3, 7, 5, 7]
print(num.count(7))

#19
arr = np.array([1.23, 2.78, 3.50, 4.11])
print(np.round(arr))

#20
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
print(np.vstack((array1, array2)))