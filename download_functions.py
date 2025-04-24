import requests
import pandas as pd

def download_LPG():

    download_url = 'https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/qus/ultimas-4-semanas-glp.csv'
    df = pd.read_csv(download_url, encoding='utf-8', sep=';')
    print('LPG: Download - Ok - 200')

    return df


def download_Gasoline_Ethanol():

    download_url = 'https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/qus/ultimas-4-semanas-gasolina-etanol.csv'
    df = pd.read_csv(download_url, encoding='utf-8', sep=';')
    print('Gasoline and Ethanol: Download - Ok - 200')

    return df


def download_Diesel_CNG():

    download_url ='https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/qus/ultimas-4-semanas-diesel-gnv.csv'
    df = pd.read_csv(download_url, encoding='utf-8', sep=';')
    print('Diesel and CNG: Download - Ok - 200')

    return df