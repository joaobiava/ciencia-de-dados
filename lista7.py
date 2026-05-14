"""
Questao 1:
A visualização de dados é o primeiro passo em qualquer análise porque permite detectar padrões, 
anomalias e distribuições que seriam invisíveis em tabelas numéricas. Antes de aplicar qualquer 
modelo, ver os dados evita erros graves.

Questao 2:
Distribuição uniforme:
    Todos os valores têm probabilidade igual
    O histograma parece uma barra plana/retangular
    Ex: resultado de um dado, número aleatório entre 0 e 1

Distribuição normal:
    Valores se concentram no centro (média)
    O histograma tem formato de sino (bell curve)
    Ex: altura de pessoas, erros de medição, notas de provas

Questao 5:
Algoritmos baseados em distância (k-NN, K-Means, SVM com kernel RBF, PCA) calculam a proximidade 
entre pontos. Se as variáveis estiverem em escalas diferentes, a variável com maior magnitude domina
o cálculo de distância, tornando as demais irrelevantes.

"""

import pandas as pd
import numpy as np
from typing import Optional
from sklearn.preprocessing import StandardScaler
import time
from tqdm import tqdm

#Questao 3
df = pd.DataFrame({'idade': [25, None, 30, None, 45, 28]})
# Imputar com a mediana
mediana = df['idade'].median()
df['idade_imputada'] = df['idade'].fillna(mediana)

print(df)

#Questao 4:
def try_or_none(value: str) -> Optional[int]:
    """Tenta converter string para int; retorna None se falhar."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

def converter_lista(strings: list[str]) -> list[Optional[int]]:
    """Aplica try_or_none em cada item da lista."""
    return [try_or_none(s) for s in strings]

# Teste
entrada = ['42', '3.14', 'abc', '100', '', None, '-7']
resultado = converter_lista(entrada)

for original, convertido in zip(entrada, resultado):
    print(f'{repr(original):>10} -> {convertido}')


# Questao 6:
# Dataset: [altura (cm), peso (kg)]
X = np.array([
    [160, 55],
    [175, 80],
    [180, 90],
    [155, 50],
    [170, 70]
])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Original:")
print(X)

print("\nNormalizado (média=0, desvio=1):")
print(X_scaled.round(2))

print(f"\nMédia original: {scaler.mean_}")
print(f"Desvio padrão:  {scaler.scale_.round(2)}")

# Questao 7:
itens = range(100)  # simula 100 tarefas

for i in tqdm(itens, desc="Processando", unit="item"):
    time.sleep(0.05)  # simula trabalho demorado

# Questao 8:
nomes = ['Alice', 'Bob', 'Carol', 'David', 'Eva']

# Opção 1: tqdm envolve a lista (recomendado)
for idx, nome in enumerate(tqdm(nomes, desc="Processando nomes")):
    time.sleep(0.3)
    print(f"  [{idx}] Olá, {nome}!")

# Opção 2: tqdm.tqdm com enumerate nativo
for idx, nome in tqdm(enumerate(nomes), total=len(nomes), desc="Alt"):
    time.sleep(0.3)
    # Aqui idx e nome funcionam normalmente

# Questao 9
epocas = 3
lotes = range(10)

for epoca in tqdm(range(epocas), desc="Épocas"):
    # leave=False faz a barra interna desaparecer ao concluir
    for lote in tqdm(lotes, desc=f"  Lote (época {epoca+1})",
                     leave=False):
        time.sleep(0.05)

#Questao 10:
tqdm.pandas(desc="Transformando")

df = pd.DataFrame({
    'texto': ['hello world', 'data science', 'python', 'pandas', 'tqdm']
})

def processar(texto: str) -> str:
    """Simula operação demorada por linha."""
    time.sleep(0.2)
    return texto.upper().replace(' ', '_')

# progress_apply = apply + barra de progresso
df['resultado'] = df['texto'].progress_apply(processar)

print(df)