import requests
import json

from resources.configs import OPENAI_API_KEY

def openai_responses(message):

    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": "Por favor, me ajude a criar um planejamento financeiro com as informações a seguir, analizando os dados e verificando se existe oportunidade para eu investir mais, reduzir os gastos com alguma despesa, e me dê conselhos para atingir meu objetivo. Você não precisa repetir as informações abaixo, da mensagem, na resposta"},
            {"role": "user", "content": message}
        ],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    result = response.json()

    response_content = result['choices'][0]['message']['content']

    print(response_content)

    return response_content


def openai_responses_metas_individuais(message):

    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": "Por favor, crie metas de investimento mensal, considerando os meus custos, e faça uma previsão de quanto de dinheiro eu terei se seguir esse planejamento. Gostaria de saber quantos anos vai demorar para eu ter 50 mil reais, 100 mil reais e, por fim, um milhão"},
            {"role": "user", "content": message}
        ],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    result = response.json()

    response_content = result['choices'][0]['message']['content']

    print(response_content)

    return response_content