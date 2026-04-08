# Exercício 1) 
# Se usa csv.reader quando o csv nao possui cabeçclho, o arquivo é muito grande ou a performance é crítica e só é necessário colunas específicas do arquivo.
# Se usa csv.DictReader quando o csv tem cabeçcalho, está mapeando os dados para um banco de dados ou objetos ou a ordem das colunas pode variar entre arquivos

# Exercício 2)
# Primeiro se consegue o HTML da página escolhida, então cir aum objeto BeautifulSoup para tranformar o HTML wm navegável. Depois é utilizado métodos como find("h2") para localizar os elementos desejados. Por fim utiliza-se get_text() para conseguir o texto

# Exercício 3)
#Usar uma API é mais comum, e pode-se acessar os dados por JSON. Já o Web Scrapping permite extrair qualuqer informação visível de uma página mesmo quando não há uma API. De forma geral API's são mais utilizados e melhores para o uso.

# Exercício 4)
# É importante manter chaves de API's seguras pois possui credenciais de acesso ao sistema. E se forem expostas, usuários terceiros podem podem utilizar estes dados de forma indevida.
# Existem algumas práticas recomendadadas como usar uma variável de ambiente e utilizar serviçõs de gerenciamento de segredos, que armazenam as chaves de forma criptografada.

# Exercício 5)
# Para coletar um grande volume de dados em tempo real, o Streaming API seria mais apropriado, pois ele mantém uma conexão contínua com o servidor e envia os tweets assim que forem publicados.

import csv
import re
from collections import Counter
import BeautifulSoup
import requests

# 1 - contagem de palavras
def contar_palavras_csv(arquivo_csv, coluna_texto):
    palavras = []
    with open(arquivo_csv, newline='', encoding='utf-8') as csvfile:
        leitor = csv.DictReader(csvfile)
    for linha in leitor:
        texto = linha[coluna_texto]
    if texto:
        texto = texto.lower()
    palavras_encontradas = re.findall(r'\b\w+\b', texto)
    palavras.extend(palavras_encontradas)
    contagem = Counter(palavras)
    top_10 = contagem.most_common(10)
    print("Top 10 palavras mais comuns:\n")
    for palavra, freq in top_10:
        print(f"{palavra}: {freq}")
contar_palavras_csv('teste.csv', 'texto')


# Exercício 2
def preco_medio_por_categoria(arquivo_csv, categoria_desejada):
    soma_precos = 0
    quantidade = 0
    with open(arquivo_csv, newline='', encoding='utf-8') as csvfile:
        leitor = csv.DictReader(csvfile)
    for linha in leitor:
        categoria = linha['categoria']
        preco = linha['preco']
        if categoria.lower() == categoria_desejada.lower():
            try:
                preco = float(preco)
                soma_precos += preco
                quantidade += 1
            except ValueError:
                continue
        if quantidade > 0:
            media = soma_precos / quantidade
            print(f"Preço médio para '{categoria_desejada}': {media:.2f}")
        else:
            print(f"Nenhum produto encontrado na categoria '{categoria_desejada}'.")
preco_medio_por_categoria('produtos.csv', 'Eletrônicos')



# Exercício 3
def extrair_h2(url):
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        titulos = soup.find_all('h2')
        print("Títulos <h2> encontrados:\n")
        for i, titulo in enumerate(titulos, 1):
            print(f"{i}. {titulo.get_text(strip=True)}")
    else:
        print("Erro ao acessar a página.")
extrair_h2("https://g1.globo.com/")