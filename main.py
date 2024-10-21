from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    Endpoint que exibe uma mensagem incrível do mundo da programação!
    '''
    return {'Hello': 'World'}

@app.get('/api/restaurantes')
def get_restaurantes(restaurante: str = Query(None)):    
    '''
    Endpoint para ver os cardápios dos restaurantes.

    Parametro restaurante: 
        (str) O nome do restaurante para buscar no cardápio. Se não for fornecido, retorna todos os restaurantes e seus cardápios.

    Retorna: 
        (dict) Se o restaurante for encontrado, retorna um dicionário com o nome do restaurante e o cardápio. Caso contrário, retorna um dicionário com a mensagem de erro.
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()

        if restaurante is None:
            return {'Dados': dados_json }

        dados_restaurante = []

        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    'item': item['Item'],
                    'preco': item['price'],
                    'descricao': item['description']
                })

        return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}

    else:
        return {'Erro': f'{response.status_code} - {response.text}'}