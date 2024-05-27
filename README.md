Proposito do codigo é gerar assinaturas em escala com base em um AD de uma empresa ou algum outro lugar onde se possa requisitar as informações dos usuarios.

Servidor.json - É um teste para buscar os dados, recomendo utilizar o json server para testar. https://www.npmjs.com/package/json-server.

API.py - É um codigo flask que faz a busca do conteudo no site(no caso o servidor.json).

Main.py - É onde contem a logica para utilizar os dados buscados e fazer o desenho na assinatura na imagem. Recomendo rodar via cmd para evitar conflito com a api.

É necessário tem uma image.jpg junto a pasta para poder criar a assinatura.

Leia o txt da pasta complementos.
