from flask import Flask, jsonify
import requests

app = Flask(__name__)

# URL do json-server(Pode alterar para o nome que achar melhor, mas é a url para buscar os dados)
JSON_SERVER_URL = 'http://localhost:3000'

@app.route('/')
def home():
    return 'Flask server is running!'

@app.route('/Usuario')
def get_usuario():
    try:
        response = requests.get(f'{JSON_SERVER_URL}/Usuario')
        response.raise_for_status()
        usuario = response.json()
        return jsonify(usuario)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
