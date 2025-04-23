import requests
import pandas as pd

def download_GLP():

    url_post = 'https://dados.gov.br/api/publico/recurso/registrar-download'

    payload = {
        'id': "99fd78e2-233d-4385-9eb2-f06f1d874fcb",
        'idConjuntoDados': "d4524519-9657-4961-9f11-bc4142f53fa8",
        'descricao': "Dados Abertos Quatro últimas semanas GLP P13.",
        'formato': "csv",
        'link': "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/qus/ultimas-4-semanas-glp.csv",
        'tipo': 1,
        'titulo': "4 ultimas semanas glp"
    }

    res = requests.post(url_post, json=payload)

    if res.status_code == 200:
        print('GLP: Download - Ok - 200')
        
        download_url = payload['link']
        df = pd.read_csv(download_url, encoding='utf-8', sep=';')
    else:
        print(f'GLP: Download - Error - {res.status_code}')


def download_Gasoline_Ethanol():

    url_post = 'https://dados.gov.br/api/publico/recurso/registrar-download'

    payload = {
        'id': "d483f3e7-837d-4d3d-ae7f-213050cd304d",
        'idConjuntoDados': "d4524519-9657-4961-9f11-bc4142f53fa8",
        'descricao': "Dados Abertos Quatro últimas semanas Etanol Hidratado + Gasolina C.",
        'formato': "csv",
        'link': "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/qus/ultimas-4-semanas-gasolina-etanol.csv",
        'tipo': 1,
        'titulo': "4 ultimas semanas gasolina etanol"
    }

    res = requests.post(url_post, json=payload)

    if res.status_code == 200:
        print('Gasoline and Ethanol: Download - Ok - 200')
        
        download_url = payload['link']
        df = pd.read_csv(download_url, encoding='utf-8', sep=';')
    else:
        print(f'Gasoline and Ethanol: Download - Error - {res.status_code}')


def download_Diesel_CNG():

    url_post = 'https://dados.gov.br/api/publico/recurso/registrar-download'

    payload = {
        'id': "5e1d2c4b-8f4e-4b36-9b5b-620430c619b5",
        'idConjuntoDados': "d4524519-9657-4961-9f11-bc4142f53fa8",
        'descricao': "Dados Abertos Quatro últimas semanas Óleo Diesel (S-500 e S-10) + GNV.",
        'formato': "csv",
        'link': "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/qus/ultimas-4-semanas-diesel-gnv.csv",
        'tipo': 1,
        'titulo': "4 ultimas semanas diesel gnv"
    }

    res = requests.post(url_post, json=payload)

    if res.status_code == 200:
        print('Diesel and CNG: Download - Ok - 200')
        
        download_url = payload['link']
        df = pd.read_csv(download_url, encoding='utf-8', sep=';')
    else:
        print(f'Diesel and CNG: Download - Error - {res.status_code}')