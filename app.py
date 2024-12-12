from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Servidor Flask en funcionamiento'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()  # Obtener los datos enviados al webhook
    print("Webhook recibido:", data)
    
    # Aquí puedes agregar lógica para procesar los datos recibidos

    return jsonify({'status': 'Webhook recibido correctamente'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
