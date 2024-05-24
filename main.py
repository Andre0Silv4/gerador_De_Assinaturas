import requests
from PIL import Image, ImageDraw, ImageFont

# URL da API Flask(pega o resultado da consulta dos Json)
API_URL = 'http://localhost:5000/Usuario'

def buscar_dados_usuarios():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        if isinstance(data, list):  # Verifica se a resposta é uma lista
            return data  # Retorna a lista diretamente
        elif isinstance(data, dict) and "Usuario" in data:  # Verifica se a resposta é um dicionário com a chave "Usuario"
            return data["Usuario"]  # Retorna a lista de usuários
        else:
            raise ValueError('Invalid data format')  # Levanta um erro se a estrutura de dados for inválida
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

def criar_imagem(agradecimento, nome, cargo, fone, empresa, id):
    # Abrir a imagem
    imagem = Image.open("image.jpg")

    # Criar um objeto ImageDraw para desenhar na imagem
    draw = ImageDraw.Draw(imagem)

    # Definir a fonte e o tamanho do texto
    fontePrimaria = ImageFont.truetype("DidactGothic-Regular.ttf", 20)
    fonteSecuncadria = ImageFont.truetype("DidactGothic-Regular.ttf", 20)
    fonteNegrito1 = ImageFont.truetype("DelaGothicOne-Regular.ttf", 20)
    fonteNegrito2 = ImageFont.truetype("DelaGothicOne-Regular.ttf", 15)

    # Definir a posição do texto na imagem(pega a cordenada x e y da imagem e começa a escrever o texto)
    posicao_agradecimento = (80, 40)
    posicao_nome = (80, 80)
    posicao_cargo = (80, 110)
    posicao_fone1 = (80, 140)
    posicao_fone2 = (215, 140)

    # Desenhar o texto na imagem
    draw.text(posicao_agradecimento, f"{agradecimento}", font=fonteSecuncadria, fill=(255, 255, 255))
    draw.text(posicao_nome, f"{nome}", font=fonteNegrito1, fill=(255, 255, 255))
    draw.text(posicao_cargo, f"{cargo}", font=fontePrimaria, fill=(255, 255, 255))
    draw.text(posicao_fone1, f"Fone: (47) 3379-", font=fontePrimaria, fill=(255, 255, 255))
    draw.text(posicao_fone2, f"{fone}", font=fonteNegrito2, fill=(255, 255, 255))

    # Salvar a assinatura alterada
    assinatura = f'Assinatura.jpg'
    imagem.save(assinatura)

if __name__ == '__main__':
    usuarios = buscar_dados_usuarios()
    for usuario in usuarios:
        criar_imagem("Atenciosamente,", usuario["nome"], usuario["cargo"], usuario["fone"], usuario["empresa"], usuario["id"])
