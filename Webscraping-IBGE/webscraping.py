# Importar bibliotecas
import re
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Fazer o request
url = "https://www.ibge.gov.br/indicadores.html"
pagina = requests.get(url)

# Filtrar e selecionar o conteudo das tabelas
soup = BeautifulSoup(pagina.content, "html.parser")

tabela = soup.find(class_="indicadores-tabela indicadores-economicos")
titulo = soup.find("th", class_="ultimo").text

rows = tabela.find_all(class_="nonsprite")
index = [id.text for id in rows]

conteudo = tabela.find_all(class_=re.compile(r"table\-accordion.+"))

ultimo = conteudo[n].find(class_="ultimo").text for n in range(len(conteudo))
anterior = conteudo[n].find(class_="desktop-tablet-only anterior").text for n in range(len(conteudo))
doze_meses = conteudo[n].find(class_="desktop-tablet-only dozemeses").text for n in range(len(conteudo))

conteudo = dict("Último": ultimo, "Anterior": anterior, "Doze meses": doze_meses)